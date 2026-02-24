import json
import os
import requests
from datetime import datetime
from typing import List, Dict, Any

class ScalpTrader:
    def __init__(self, config_path: str, state_path: str, log_dir: str):
        self.config_path = config_path
        self.state_path = state_path
        self.log_dir = log_dir
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        with open(state_path, 'r') as f:
            self.state = json.load(f)
        self.product_id = self.config['product_id']

    def get_candles(self, granularity: int = 300) -> List[List[float]]:
        """Fetch 5-minute candles from Coinbase public API"""
        url = f"https://api.exchange.coinbase.com/products/{self.product_id}/candles"
        params = {
            'granularity': granularity,
            'limit': 100
        }
        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            return resp.json()  # [timestamp, low, high, open, close, volume]
        except Exception as e:
            print(f"[SCALP] Error fetching candles: {e}")
            return []

    def calculate_rsi(self, candles: List[List[float]], periods: int = 14) -> float:
        """Calculate RSI from closes"""
        if len(candles) < periods + 1:
            return 50.0
        sorted_candles = sorted(candles, key=lambda x: x[0])
        closes = [c[4] for c in sorted_candles]
        deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
        gains = [d if d > 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]
        avg_gain = sum(gains[-periods:]) / periods
        avg_loss = sum(losses[-periods:]) / periods
        if avg_loss == 0:
            return 100.0
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def calculate_vwap(self, candles: List[List[float]]) -> float:
        """Calculate VWAP"""
        typical_prices = [(c[1] + c[2] + c[4]) / 3 for c in candles]
        volumes = [c[5] for c in candles]
        if sum(volumes) == 0:
            return typical_prices[-1] if typical_prices else 0
        return sum(tp * vol for tp, vol in zip(typical_prices, volumes)) / sum(volumes)

    def check_volume_spike(self, candles: List[List[float]], threshold: float = 1.5) -> bool:
        """Check if recent volume > 150% of average"""
        if len(candles) < 20:
            return False
        volumes = [c[5] for c in candles]
        recent_vol = sum(volumes[-3:]) / 3
        avg_vol = sum(volumes[:-3]) / (len(volumes) - 3)
        if avg_vol == 0:
            return False
        return (recent_vol / avg_vol) > threshold

    def can_enter_new_position(self) -> bool:
        """Check if we already have open scalp or traded today"""
        today = datetime.now().strftime('%Y-%m-%d')
        scalp_state = self.state.get('scalp', {})
        if scalp_state.get('position_size', 0) > 0:
            return False
        last_date = scalp_state.get('last_trade_date')
        if last_date == today:
            return False
        return True

    def check_exit(self, current_price: float) -> bool:
        """Check if we hit 2% profit target"""
        scalp = self.state.get('scalp', {})
        if not scalp or scalp.get('position_size', 0) == 0:
            return False
        entry_price = scalp['entry_price']
        target = entry_price * 1.02
        return current_price >= target

    def execute_buy(self, amount_usd: float, price: float):
        """Execute paper scalp buy"""
        size = amount_usd / price
        if 'scalp' not in self.state:
            self.state['scalp'] = {}
        self.state['scalp'] = {
            'position_size': size,
            'entry_price': price,
            'entry_time': datetime.now().isoformat(),
            'entry_date': datetime.now().strftime('%Y-%m-%d'),
            'target_price': price * 1.02,
            'invested_usd': amount_usd,
            'status': 'OPEN'
        }
        self.save_state()
        self.log_trade('SCALP_BUY', amount_usd, size, price)
        print(f"[SCALP] ✅ BUY {size:.6f} SOL @ ${price:.2f} (Target: ${price * 1.02:.2f})")

    def execute_sell(self, price: float):
        """Execute paper scalp sell"""
        scalp = self.state.get('scalp', {})
        size = scalp['position_size']
        entry_price = scalp['entry_price']
        proceeds = size * price
        pnl = proceeds - scalp['invested_usd']
        pnl_pct = (pnl / scalp['invested_usd']) * 100
        self.state['cash'] = self.state.get('cash', 0) + proceeds
        self.state['scalp'] = {
            'position_size': 0,
            'last_trade_date': datetime.now().strftime('%Y-%m-%d'),
            'last_exit_price': price,
            'last_pnl_usd': round(pnl, 2),
            'last_pnl_pct': round(pnl_pct, 2),
            'status': 'CLOSED'
        }
        self.save_state()
        self.log_trade('SCALP_SELL', proceeds, size, price, pnl=pnl)
        print(f"[SCALP] ✅ SELL {size:.6f} SOL @ ${price:.2f} | PnL: ${pnl:.2f} ({pnl_pct:+.1f}%)")

    def log_trade(self, action: str, usd_amount: float, size: float, price: float, pnl: float = None):
        """Log to JSONL"""
        log_file = os.path.join(self.log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.jsonl")
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "product": self.product_id,
            "mode": "paper",
            "usd_amount": round(usd_amount, 2),
            "size": round(size, 6),
            "price": round(price, 2)
        }
        if pnl is not None:
            entry['pnl_usd'] = round(pnl, 2)
        with open(log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def save_state(self):
        with open(self.state_path, 'w') as f:
            json.dump(self.state, f, indent=2)

    def run(self):
        """Main entry point"""
        if not self.config.get('scalp_enabled', False):
            return
        candles = self.get_candles()
        if len(candles) < 50:
            print("[SCALP] ⚠️ Not enough data")
            return
        current_price = candles[-1][4]  # Check exit first
        if self.state.get('scalp', {}).get('position_size', 0) > 0:
            if self.check_exit(current_price):
                self.execute_sell(current_price)
            else:
                target = self.state['scalp']['target_price']
                print(f"[SCALP] ⏳ Holding for target. Current: ${current_price:.2f}, Target: ${target:.2f}")
                return  # Check entry
        if not self.can_enter_new_position():
            print("[SCALP] ⏸️ Already traded today or position open")
            return
        rsi = self.calculate_rsi(candles)
        vwap = self.calculate_vwap(candles)
        vol_spike = self.check_volume_spike(candles)
        below_vwap = current_price < vwap
        print(f"[SCALP] 📊 RSI: {rsi:.1f} (<30?), Price: ${current_price:.2f}, VWAP: ${vwap:.2f} (Below? {below_vwap}), VolSpike: {vol_spike}")
        if rsi < 30 and below_vwap and vol_spike:
            amount = self.config.get('scalp_amount_usd', 5.0)
            if self.state.get('cash', 0) >= amount:
                self.execute_buy(amount, current_price)
            else:
                print(f"[SCALP] ❌ Insufficient cash (${self.state.get('cash', 0):.2f})")
        else:
            print("[SCALP] ❌ Conditions not met, skipping")

if __name__ == '__main__':
    trader = ScalpTrader('config.json', 'state.json', 'logs')
    trader.run()
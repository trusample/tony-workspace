from datetime import datetime
import json
import requests

# Load state
with open('state.json', 'r') as f:
    state = json.load(f)

# Configuration
with open('config.json', 'r') as f:
    config = json.load(f)

def execute_dca_buy():
    amount_usd = config['buy_usd']
    product_id = config['product_id']
    # Implement the buy logic here (API call)
    print(f"Executing DCA buy of ${amount_usd} for {product_id}")

# Logic to execute DCA first
last_buy_date = state.get('last_buy_date')
today = datetime.now().strftime('%Y-%m-%d')

if today != last_buy_date:
    execute_dca_buy()
    state['last_buy_date'] = today  # Update last_buy_date
    with open('state.json', 'w') as f:
        json.dump(state, f, indent=2)

# SCALP MODULE INTEGRATION
print("\n" + "="*50)
print("Checking Scalp Opportunity...")
print("="*50)
try:
    from scalp_module import ScalpTrader
    scalp_trader = ScalpTrader(
        config_path='config.json',
        state_path='state.json',
        log_dir='logs'
    )
    scalp_trader.run()
except Exception as e:
    print(f"[SCALP] Error: {e}")
    import traceback
    traceback.print_exc()
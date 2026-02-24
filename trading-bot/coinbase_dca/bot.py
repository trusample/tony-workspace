
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
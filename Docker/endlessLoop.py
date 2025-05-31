import time
# Run forever
while True:
    try:
        time.sleep(1200)  # Sleep to avoid high CPU usage
    except Exception:
        print("\nException re-run in loop anyway...")

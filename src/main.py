from config import APP_NAME, VERSION, BASE_RPC
from monitor import start_monitor

print("=" * 40)
print(APP_NAME)
print("Version:", VERSION)
print("=" * 40)

print("Connecting to Base...")
print(BASE_RPC)

start_monitor()
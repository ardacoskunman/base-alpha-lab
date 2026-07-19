import time

from base_client import get_latest_block


def start_monitor():

    print("Starting Base Monitor...")

    last_block = None

    while True:

        current_block = get_latest_block()

        if last_block is None:

            last_block = current_block

            print(f"Current block: {current_block}")

        elif current_block > last_block:

            print()
            print("🟢 New block detected!")
            print(current_block)

            last_block = current_block

        time.sleep(2)
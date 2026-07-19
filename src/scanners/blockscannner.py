from datetime import datetime

from base_client import get_block_by_number


def scan_block(block_number):

    block_data = get_block_by_number(block_number)

    if block_data is None:
        print(f"Block {block_number} not found.")
        return

    timestamp = int(block_data["timestamp"], 16)
    readable_time = datetime.fromtimestamp(timestamp)

    print("=" * 50)
    print(f"Block Number : {block_number}")
    print(f"Hash         : {block_data['hash']}")
    print(f"Timestamp    : {readable_time}")
    print(f"Transactions : {len(block_data['transactions'])}")
    print("=" * 50)

    for tx in block_data["transactions"]:

        to_address = tx["to"]

        if to_address is None:
            to_address = "🆕 Contract Creation"

        value_eth = int(tx["value"], 16) / 10**18

        print(f"Hash : {tx['hash']}")
        print(f"From : {tx['from']}")
        print(f"To   : {to_address}")
        print(f"ETH  : {value_eth}")
        print("-" * 50)
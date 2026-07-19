import requests

from config import BASE_RPC


def send_rpc_request(method, params=None):
    if params is None:
        params = []

    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }

    response = requests.post(BASE_RPC, json=payload)
    response.raise_for_status()

    return response.json()


def get_latest_block():
    result = send_rpc_request("eth_blockNumber")

    return int(result["result"], 16)
def get_block_by_number(block_number):

    
    hex_block_number = hex(block_number)

    result = send_rpc_request("eth_getBlockByNumber", [hex_block_number, True])

    return result["result"]
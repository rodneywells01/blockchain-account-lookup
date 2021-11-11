import time 
import json
import asyncio
import websockets

# from websocket import create_connection
# import websocket



# https://www.coinapi.io/
COIN_API_IO_KEY = "C0FE026C-BAFA-4414-B342-6E9F50D9E2D1"
URLS = { 
    "sandbox": "ws://ws-sandbox.coinapi.io/v1/",
    "production": "ws://ws.coinapi.io/v1/"
}

# COIN_API_IO_URL = URLS["production"]
COIN_API_IO_URL = URLS["sandbox"]

hello_payload = {
  "type": "hello",
  "apikey": COIN_API_IO_KEY,
  "heartbeat": False,
  "subscribe_data_type": ["quote"],
  # "subscribe_filter_asset_id": ["BTC", "ETH"]
  "subscribe_filter_asset_id": ["BTC"]
}


async def hello():
    async with websockets.connect(COIN_API_IO_URL) as websocket:
        while True: 
            await websocket.send(
                json.dumps(hello_payload))
            res = await websocket.recv()
            # res = websocket.recv()
            print(res)
            time.sleep(1)


asyncio.run(
    hello()
)

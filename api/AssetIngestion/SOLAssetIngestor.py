from api.AssetIngestion.AssetIngestor import AssetIngestor


from solana.publickey import PublicKey
from solana.rpc.api import Client


class SOLAssetIngestor(AssetIngestor): 
	SOL_PER_LAMPORT = 0.000000001
	COIN_ID = "solana"

	def __init__(self):
		pass

	def fetch_account_assets(self, account_id): 
		res = http_client.get_account_info(
			PublicKey(account_id),
			encoding = "jsonParsed",
		)

		sol_balance = res["result"]["value"]["lamports"] * SOL_PER_LAMPORT
		print(sol_balance)


		return {
			"token_type": "SOL".
			"token_balance": sol_balance, 
			"NFTS": ["TODO"], 
		}

	def get_current_asset_info(self):
		"""
		Get the current price in USD for a given coin id. 
		"""
		url = f"https://api.coingecko.com/api/v3/coins/{self.COIN_ID}?localization=false&tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true"
		response = requests.request("GET", url)
		return response.json()["market_data"]["current_price"]["usd"]



	

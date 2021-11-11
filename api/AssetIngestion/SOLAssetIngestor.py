from api.AssetIngestion.AssetIngestor import AssetIngestor


from solana.publickey import PublicKey
from solana.rpc.api import Client


class SOLAssetIngestor(AssetIngestor): 
	SOL_PER_LAMPORT = 0.000000001

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
		pass


	

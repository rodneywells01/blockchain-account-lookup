from solana.publickey import PublicKey
from solana.rpc.api import Client

http_client = Client("https://api.mainnet-beta.solana.com")

sol_per_lamport = 0.000000001


"""
Get account info being used here 
https://github.com/michaelhly/solana-py/blob/751bcf7b6697b744e1e7bdc4c25b45f7dc282d9a/src/solana/rpc/core.py#L72


"""


# http_client.get_account_info(
# 	pubkey: Union[PublicKey, str],
#     commitment: Optional[Commitment] = None,
#     encoding: str = "base64",
#     data_slice: Optional[types.DataSliceOpts] = None
# )


# solana_client.get_confirmed_transaction("3PtGYH77LhhQqTXP4SmDVJ85hmDieWsgXCUbn14v7gYyVYPjZzygUQhTk3bSTYnfA48vCM1rmWY7zWL3j1EVKmEy") 


# res = http_client.get_confirmed_transaction("46fwF8SSFhum2BWJMVzkYxuxW2Nrrs1Typa38bPuzA7tqzFQRGaqpQJo83DdaH61vqCVsiW6PtLtoEuwaQzMK6ZX")
# print(res)


res = http_client.get_account_info(
	PublicKey("6sFdGABSP5FA3Lx8i473zBeEGn5uAS7h7wprwj9nWVaz"),
    encoding = "jsonParsed",
)

print(res)

sol_balance = res["result"]["value"]["lamports"] * sol_per_lamport
print(sol_balance)

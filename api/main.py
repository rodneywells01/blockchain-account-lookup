from solana.publickey import PublicKey
from solana.rpc.api import Client

import logging
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    logging.info("Hello, world!!")
    return "Index Page"


@app.route("/hello")
def hello():
    logging.info("Hello, world!1")
    return {"message": "hello, world! blockchain"}


@app.route("/sol/<account>")
def get_sol_account_value(account):
    """
    Fetch the amount of SOL that a given account has. 
    """
    http_client = Client("https://api.mainnet-beta.solana.com")
    SOL_PER_LAMPORT = 0.000000001

    res = http_client.get_account_info(
        PublicKey(account),
        encoding = "jsonParsed"
    )

    try:
        sol_balance = res["result"]["value"]["lamports"] * SOL_PER_LAMPORT
    except Exception: 
        return {
            "error": f"Could not find SOL Balance for Account",
            "account": account
        }

    return {
        "sol_balance": sol_balance,
        "account": account
    }


    
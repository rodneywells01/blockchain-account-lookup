import os 

from solana.publickey import PublicKey
from solana.rpc.api import Client

import logging
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

import requests


from extensions import db 


# Initial Flask configuration. 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@postgres:5432/pantry"  # TODO - do not store here
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# migrate = Migrate(app, db)
auth = HTTPBasicAuth()

from models.User import User

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
        "account": account,
        "current_coin_price": get_current_asset_info("solana")
    }

@app.route('/users', methods = ['POST'])
def new_user():
    """
    Register a new user for the app. 
    """
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}


@app.route('/api/resource')
@auth.login_required
def get_accounts():
    return jsonify({ 'data': 'Hello, %s!' % g.user.username })

@auth.verify_password
def verify_password(username, password):
    # https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
    user = User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True



def get_current_asset_info(coin_id):
    """
    Get the current price in USD for a given coin id. 
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false&tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true"
    response = requests.request("GET", url)
    return response.json()["market_data"]["current_price"]["usd"]

    
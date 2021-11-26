from passlib.apps import custom_app_context as pwd_context

from extensions import db


# https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

class UserAccount(db.Model):
    __tablename__ = 'user_accounts'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer) 
    account_id = db.Column(db.String(64))
    asset_type = db.Column(db.String(5))



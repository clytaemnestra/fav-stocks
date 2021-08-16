from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    hash = db.Column(db.Integer(), nullable=False)
    cash = db.Column(db.Integer())


class TransactionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer(), nullable=False)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey(Account.id), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey(Stock.id), nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False)
    transaction_id = (db.Integer, db.ForeignKey(TransactionType.id))

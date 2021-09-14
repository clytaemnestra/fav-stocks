from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    hash = db.Column(db.String(120), nullable=False)
    balance = db.Column(db.Numeric())


class TransactionTypesPostgresEnum(enum.Enum):
    BUY = 'buy'
    SELL = 'sell'


class TransactionType(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.Enum(TransactionTypesPostgresEnum, create_type=False), nullable=False)


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(), nullable=False)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.TIMESTAMP, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey(Account.id), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey(Stock.id), nullable=False)
    transaction_type_id = (db.Integer, db.ForeignKey(TransactionType.id))


class Ownership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey(Account.id))
    stock_id = db.Column(db.Integer, db.ForeignKey(Stock.id))
    amount = db.Column(db.Integer, nullable=False)


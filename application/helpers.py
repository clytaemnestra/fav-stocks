from functools import wraps
from flask import g, request, redirect, url_for, session
import re
from .models import Account, Stock, db, Ownership
from decimal import *
from numbers import Number


def login_required(f):
    """
    Makes sure that only logged in user can access the content.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def check_password_requirements(password: int, confirmation: int) -> bool:
    """Checks if password satisfies requirements."""
    if password == confirmation \
            and re.search("[A-Z]", password) \
            and re.search("[0-9]", password) \
            and len(password) > 8:
        return True
    else:
        return False


def user_exists(username: str) -> bool:
    """Checks if user already exists."""
    user = Account.query.filter(Account.username == username).all()
    if len(user) == 1:
        return True
    else:
        return False


def stock_exists(stock_symbol: str) -> bool:
    """Checks if stock exists."""
    existing_stock = Stock.query.filter(stock_symbol == Stock.name).all()
    if len(existing_stock) >= 1:
        return True
    else:
        return False


def check_remaining_cash(username: str) -> Number:
    """Checks how much of cash user has."""
    remaining_cash = db.session.query(Account.balance).filter(Account.username == username).limit(1).all()
    return remaining_cash[0][0]


def check_stock_price(stock: str) -> Number:
    """Checks stock price."""
    stock_price = db.session.query(Stock.price).filter(Stock.name == stock).limit(1).all()
    return stock_price[0][0]


def check_user_owns_stock(user: str, stock: str) -> bool:
    """Checks if user already owns stock."""
    user_owns_stock = db.session.query(Ownership.amount) \
        .filter(Ownership.account_id == Account.id) \
        .filter(Ownership.stock_id == Stock.id) \
        .filter(Stock.name == stock) \
        .filter(Account.username == user) \
        .all()
    if len(user_owns_stock) == 1:
        return True
    else:
        return False


def check_stock_amount_owned(user: str, stock: str) -> int:
    """Check amount of given stock that user owns."""
    amount = db.session.query(Ownership.amount) \
        .filter(Ownership.account_id == Account.id) \
        .filter(Ownership.stock_id == Stock.id) \
        .filter(Stock.name == stock) \
        .filter(Account.username == user) \
        .all()[0][0]
    return amount


def check_owned_stocks(user: str) -> list:
    owned_stocks = db.session.query(Stock.name, Stock.price, Ownership.amount) \
        .filter(Ownership.account_id == Account.id) \
        .filter(Ownership.stock_id == Stock.id) \
        .filter(Account.username == user) \
        .all()
    return owned_stocks

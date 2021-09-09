from functools import wraps
from flask import g, request, redirect, url_for, session
import re
from .models import Account, Stock, db


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


def check_password_requirements(password, confirmation):
    """Checks if password satisfies requirements."""
    if password == confirmation \
            and re.search("[A-Z]", password) \
            and re.search("[0-9]", password) \
            and len(password) > 8:
        return True
    else:
        return False


def user_exists(username):
    """Checks if user already exists."""
    user = Account.query.filter(Account.username == username).all()
    if len(user) == 1:
        return True
    else:
        return False


def stock_exists(stock_symbol):
    """Checks if stock exists."""
    existing_stock = Stock.query.filter(stock_symbol == Stock.name).all()
    if len(existing_stock) >= 1:
        return True
    else:
        return False


def check_remaining_cash(username):
    """Checks how much of cash user has."""
    remaining_cash = db.session.query(Account.balance).filter(Account.username == username).limit(1).all()
    remaining_cash_int = int(remaining_cash[0][0])
    return remaining_cash_int


def check_stock_price(stock):
    """Checks stock price."""
    stock_price = db.session.query(Stock.price).filter(Stock.name == stock).limit(1).all()
    stock_price_int = int(stock_price[0][0])
    return stock_price_int

from flask import Blueprint, render_template, request, session, flash
from .helpers import *
from sqlalchemy.sql import select
from .models import Account, db, Stock, Ownership, Transaction
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import logging

logging.basicConfig()
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.DEBUG)

app = Blueprint('app', __name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/")
@login_required
def index():
    """Show homepage."""
    logged_user = session["user_id"]
    owned_stocks = check_owned_stocks(logged_user)
    print(type(owned_stocks))
    return render_template("index.html", owned_stocks=owned_stocks)


@app.route("/register", methods=["GET", "POST"])
def register_user():
    """Register user in the database."""
    if request.method == "POST":
        username = request.form.get('username')
        confirmation = request.form.get('confirmation')
        password = request.form.get('password')

        # in case of empty input
        if not username or not password or not confirmation:
            flash("Please fill in all required fields.")
            return render_template("register.html"), 400

        # in case password doesn't meet complexity requirements
        if not check_password_requirements(password, confirmation):
            flash("Password must match complexity requirements: minimum 8 characters, a capital letter and a number.")
            return render_template("register.html"), 403

        # check if user already exists
        elif user_exists(username=username):
            flash("User already exists.")
            return render_template("register.html"), 400

        else:
            try:
                # create new account and add it to the database
                password_hash = generate_password_hash(password)
                new_account = Account(username=username, hash=password_hash, balance=10000)
                db.session.add(new_account)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(str(e))
        return redirect("/login")
    else:
        # GET request
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Logs user in, by remembering his username within the session"""
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        hash = db.session.query(Account.hash).filter(Account.username == username).limit(1).all()

        # in case of empty input
        if not username or not password:
            flash("Please fill in all required fields.")
            return render_template("login.html"), 400

        # check if user already exists
        elif not user_exists(username=username):
            flash("User doesn't exist. Please register first.")
            return render_template("register.html"), 403

        # check if password is correct
        elif not check_password_hash(hash[0]["hash"], password):
            flash("Invalid password"), 403
            print("pw:", password)
            print("hash", hash)
            return render_template("login.html")
        else:
            session["user_id"] = username
            # logs user in and displays homepage
            return redirect("/")
    else:
        # GET request
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Logs user out."""
    session.clear()
    return redirect("/login")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        stock_symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # check if input is empty
        if not stock_symbol or not shares:
            flash("Input cannot be empty.", 400)
            return redirect("/buy")

        # check if user entered a valid number
        elif int(shares) <= 0:
            flash("Please enter valid whole number.", 400)
            return redirect("/buy")

        # check if stock exists
        elif not stock_exists(stock_symbol):
            flash("Please enter valid stock symbol.", 400)
            return redirect("/buy")

        # check if user has enough of remaining balance
        elif check_remaining_cash(session["user_id"]) < check_stock_price(stock_symbol) * int(shares):
            flash("You don't have enough of balance for the given purchase.", 400)
            return redirect("/buy")

        else:
            try:
                # perform purchase
                amount = check_stock_price(stock_symbol) * int(shares)
                account_id = \
                    db.session.query(Account.id).filter(Account.username == session["user_id"]).limit(1).all()[0][0]
                stock_id = db.session.query(Stock.id).filter(Stock.name == stock_symbol).limit(1).all()[0][0]
                new_transaction = \
                    Transaction(time=datetime.now(), amount=amount, account_id=account_id, stock_id=stock_id)
                db.session.add(new_transaction)

                # update users balance
                updated_amount = check_remaining_cash(session["user_id"]) - amount
                user = db.session.query(Account).filter(Account.username == session["user_id"]).one()
                user.balance = updated_amount

                # update the table ownership
                user_owner = \
                    db.session.query(Account.username).filter(Account.username == session["user_id"]).limit(1).all()[0][
                        0]

                # in case user already owns the stock
                if check_user_owns_stock(user_owner, stock_symbol):
                    amount_owned_stocks = check_stock_amount_owned(user_owner, stock_symbol)
                    updated_amount = int(amount_owned_stocks) + int(shares)
                    db.session.query(Ownership) \
                        .filter(Ownership.account_id == Account.id) \
                        .filter(Ownership.stock_id == Stock.id) \
                        .filter(Stock.name == stock_symbol) \
                        .filter(Account.username == session["user_id"]) \
                        .update({'amount': updated_amount}, synchronize_session='fetch')
                    db.session.commit()
                    return redirect("/buy")

                else:
                    add_ownership = Ownership(account_id=account_id, stock_id=stock_id, amount=shares)
                    db.session.add(add_ownership)
                    db.session.commit()
                    return redirect("/buy")

            except Exception as e:
                db.session.rollback()
                return redirect("/")
    else:
        # GET request
        return render_template("buy.html")

#
# @app.route("/sell", methods == ["GET", "POST"])
# @login_required
# def sell():
#     if request.method == "GET":
#         stocks =

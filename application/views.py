from flask import Blueprint, render_template, request, session, flash
from .helpers import *
from sqlalchemy.sql import select
from .models import Account, db
from werkzeug.security import generate_password_hash, check_password_hash
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
    owned_stocks = db.session.query(Stock.name, Stock.price, Ownership.amount) \
        .filter(Ownership.account_id == logged_user).all()
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
                password_hash = generate_password_hash(password)
                new_account = Account(username=username, hash=password_hash, cash=10000, balance=10000)
                print("user created", username, password_hash)
                db.session.add(new_account)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(str(e))
        return redirect("/login")
    else:
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

        elif not check_password_hash(hash[0]["hash"], password):
            flash("Invalid password"), 403
            print("pw:", password)
            print("hash", hash)
            return render_template("login.html")
        else:
            session["user_id"] = username
            return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Logs user out."""
    session.clear()
    return redirect("/login")

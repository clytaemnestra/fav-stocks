from flask import Blueprint, render_template, request, session, flash
from .helpers import *
from sqlalchemy.sql import select
from .models import Account, db
from werkzeug.security import generate_password_hash
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
        print(username)
        print(confirmation)
        print(password)

        # in case of empty input
        if empty_input(username, password, confirmation):
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
                counter = 1
                password_hash = generate_password_hash(password)
                new_account = Account(id=+counter, username=username, hash=password_hash, cash=10000, balance=10000)
                print("user created", username, password_hash)
                db.session.add(new_account)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(str(e))
        return redirect("/")
    else:
        return render_template("register.html")

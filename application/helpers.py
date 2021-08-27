from functools import wraps
from flask import g, request, redirect, url_for
import re
from .models import Account


def login_required(f):
    """
    Makes sure that only logged in user can access the content.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
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

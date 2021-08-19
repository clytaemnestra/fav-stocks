from functools import wraps
from flask import g, request, redirect, url_for


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

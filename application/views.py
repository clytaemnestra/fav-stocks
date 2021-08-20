from flask import Blueprint, render_template, request
from .helpers import login_required

app = Blueprint('app', __name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/")
@login_required
def index():
    """Show homepage."""
    rows = ...
    return render_template("index.html", rows=rows)


@app.route("/register", methods=["GET", "POST"])
def register_user():
    """Register user in the database."""
    if request.method == "POST":
        pass
        return redirect("/")
    else:
        return render_template("register.html")




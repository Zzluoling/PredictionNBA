from flask import Blueprint, render_template
from flask_login import current_user, login_required

main = Blueprint("index", __name__)


@main.route("/")
@login_required
def index():
    return render_template("index.html", username=current_user.username)

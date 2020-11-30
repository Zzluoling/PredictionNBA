from flask import Blueprint, render_template, request, redirect, url_for, flash
from service.User import *
from flask_login import logout_user

log = Blueprint("log", __name__)


@log.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.getUserByPassword(username, password)
        print(user)
        if user is None:
            return render_template("login.html")
        else:
            login_user(user)
            return redirect(url_for("index.index"))
    return render_template("login.html")


@log.route("/logout")
def logout():
    logout_user()
    flash("goodbye")
    return redirect(url_for('log.login'))

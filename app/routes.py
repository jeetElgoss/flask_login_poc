from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app import app, db, login_manager
from app.models import User
from app.forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', form=form, error='Invalid username or password')
#
#
# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
#

@app.route("/")
# @login_required
def index():
    return render_template("index.html")

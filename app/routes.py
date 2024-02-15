from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from app import app, login_manager
from app.models import User
from app.forms import LoginForm, RegistrationForm
from .services.register_service import UserAccount


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=['POST', "GET"])
def register():
    new_form = RegistrationForm()
    if request.method == "POST":
        if new_form.validate_on_submit():
            result = UserAccount.register(UserAccount, new_form)
            return jsonify({"data": result})
    else:
        return render_template("registration.html", form=new_form)


@app.route("/login", methods=["GET", "POST"])
def login():
    credentials = LoginForm()
    if request.method == "POST":
        if credentials.validate_on_submit():
            result = UserAccount.login(UserAccount, credentials)
            print(result)
            exit()
            if result:
                login_user(result)
                return jsonify({"data": "You are logged in!"})
    else:
        return render_template('login.html', form=credentials, error='Invalid username or password')


@app.route("/")
# @login_required
def index():
    return render_template("index.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

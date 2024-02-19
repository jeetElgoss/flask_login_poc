from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, login_required
from app import app, login_manager
from models.account_model import User
from app.forms import LoginForm, RegistrationForm
from .services.user_account_service import UserAccount


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=['POST', "GET"])
def register():
    form_data = RegistrationForm()
    if request.method == "POST":
        if form_data.validate_on_submit():
            result = UserAccount.register(UserAccount, form_data)
            return jsonify({"data": result})
    else:
        return render_template("registration.html", form=form_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    form_data = LoginForm()
    if request.method == "POST":
        if form_data.validate_on_submit():
            result = UserAccount.login(UserAccount, form_data)
            if result:
                login_user(result)
                return jsonify({"data": "You are logged in!", "redirect_url": "/"})
    else:
        return render_template('login.html', form=form_data)


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

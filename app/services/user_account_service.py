from passlib.hash import sha256_crypt
from models.account_model import User
from . import db

class UserAccount:
    @staticmethod
    def register(cls, form_data):
        # Hash the password before storing it
        hashed_password = sha256_crypt.hash(form_data.password.data)
        # Create a new user
        new_user = User(username=form_data.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return "User registration is done success!"

    @staticmethod
    def login(clf, form_data):
        user = User.query.filter_by(username=form_data.username.data).first()
        if user and sha256_crypt.verify(form_data.password.data, user.password):
            return user
        else:
            return "username or password do not match"

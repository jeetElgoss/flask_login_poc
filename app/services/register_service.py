from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import User


class UserAccount:
    @staticmethod
    def register(cls, form):
        # Hash the password before storing it
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        # Create a new user
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return "User registration is done success!"

    @staticmethod
    def login(clf, credentials):
        user = User.query.filter_by(username=credentials.username).first()
        # Hash the password before storing it
        hashed_password = generate_password_hash(credentials.password.data, method='pbkdf2:sha256')
        if user and check_password_hash(user.password_hash, hashed_password):
            print(f"{user.password_hash} = {hashed_password}")
            return user
        else:
            return "username or password do not match"

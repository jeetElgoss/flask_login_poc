from . import db
import flask_login

class Student(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Dob = db.Column(db.String(30))
    Fee = db.Column(db.Integer)
    CreatedOn = db.Column(db.Date)







from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String(100))
    species = db.Column(db.String(100))
    breed = db.Column(db.String(100))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer)
    password = db.Column(db.String(8))
    email = db.Column(db.String(100))

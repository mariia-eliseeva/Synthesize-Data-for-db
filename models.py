from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128))


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    inn = db.Column(db.String(12), unique=True, nullable=False)
    responsible_person = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(20), default='Не в работе')

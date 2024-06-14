from datetime import datetime
from app import db
from models import Client, User


def add_client():
    user1 = User.query.filter_by(login='ivan').first()
    user2 = User.query.filter_by(login='petr').first()

    clients = [
        Client(account_number="1", last_name="Никитин", first_name="Никита", patronymic="Никитич",
               birth_date=datetime.strptime("2000-01-01", "%Y-%m-%d").date(), inn="1",
               responsible_person=user1.full_name if user1 else '', status="Не в работе"),
        Client(account_number="2", last_name="Добрынев", first_name="Добрыня", patronymic="Добрыневич",
               birth_date=datetime.strptime("2000-01-01", "%Y-%m-%d").date(), inn="2",
               responsible_person=user2.full_name if user2 else '', status="Не в работе")
    ]
    db.session.bulk_save_objects(clients)
    db.session.commit()


if __name__ == '__main__':
    from app import app
    with app.app_context():
        add_client()

from app import db
from models import User


def add_user():
    users = [
        User(full_name='Администратор', login='admin', password='admin'),
        User(full_name='Иван Иванович', login='ivan', password='ivan'),
        User(full_name='Петр Петрович', login='petr', password='petr')
    ]
    db.session.bulk_save_objects(users)
    db.session.commit()


if __name__ == '__main__':
    from app import app
    with app.app_context():
        add_user()

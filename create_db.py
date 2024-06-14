from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        from add_user import add_user
        from add_client import add_client
        add_user()
        add_client()

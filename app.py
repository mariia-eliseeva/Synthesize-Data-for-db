from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Client, User
from flask_login import LoginManager, login_user, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = User.query.filter_by(login=login).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid login credentials')
    return render_template('login.html')


@app.route('/clients')
@login_required
def clients():
    clients = Client.query.filter_by(responsible_person=current_user.full_name).all()
    return render_template('clients.html', clients=clients)


@app.route('/update_status/<int:id>', methods=['POST'])
def update_status(id):
    client = Client.query.get_or_404(id)
    client.status = request.form['status']
    db.session.commit()
    return redirect(url_for('dashboard'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/dashboard')
@login_required
def dashboard():
    clients = Client.query.filter_by(responsible_person=current_user.full_name).all()
    print(clients)
    return render_template('clients.html', clients=clients)


if __name__ == '__main__':
    app.run(debug=True)

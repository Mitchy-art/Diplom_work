from flask import Flask, render_template, redirect, url_for, request
from models import db, Pet, User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_url_path='/static/css_pack')
app.config['SECRET_KEY'] = 'j7u83u7b5n76b7n8mm9c3s'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def main_page_f():
    return render_template('f_task/main_page.html', pets=Pet)


@app.route('/shop')
def shop():
    db.create_all()
    pets = Pet.query.all()
    return render_template('f_task/shop_page.html', pets=pets)


@app.route('/cart_page')
def cart():
    return render_template('f_task/cart_page.html', pets=Pet)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['Введите логин']
        age = request.form['Введите возвраст']
        password = request.form['Введите пароль']
        confirm_password = request.form['Повторите пароль']
        email = request.form['Введите почту']
        if len(username) <= 30 and password == confirm_password and len(password) >= 8 and age.isdigit() and len(
                age) <= 3 and len(email) >= 10:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, password=hashed_password, age=int(age), email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main_page_f'))
    return render_template('f_task/registration_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main_page'))
    return render_template('f_task/enter_page.html')


if __name__ == '__main__':
    app.run(debug=True)

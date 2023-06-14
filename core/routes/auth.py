from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from ..models import User
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        print(user.username)
        print(check_password_hash(user.password, password))

        if user and check_password_hash(user.password, password):
            login_user(user)
            print('logged in')
            return redirect(url_for('main.index'))
        else:
            print('login failed')
            return redirect(url_for('auth.login'))
    
    context = {
        'title': 'Login | Store Name',
    }

    return render_template(
        'auth/login.html',
        **context
    )

@auth.route('/logout/', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/change-password/', methods=['GET'])
def register():
    return 'change password'
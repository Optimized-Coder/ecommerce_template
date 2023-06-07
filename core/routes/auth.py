from flask import Blueprint, render_template
from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__, url_prefix='/admin')

@auth.route('/login/', methods=['GET'])
def login():
    return render_template('auth/login.html')

@auth.route('/logout/', methods=['GET'])
def logout():
    logout_user()

@auth.route('/change-password/', methods=['GET'])
def register():
    return 'change password'
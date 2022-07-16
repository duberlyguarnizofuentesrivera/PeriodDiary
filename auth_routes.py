import flask_login
from flask import Blueprint, request, render_template, redirect
from flask_login import login_user

from models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login_page():
    username = request.form['user']
    password = request.form['pass']
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        pass
    else:
        login_user(user, remember=True)
        return redirect('/')
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return redirect('/login')

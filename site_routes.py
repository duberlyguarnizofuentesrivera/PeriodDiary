from datetime import date

import flask_login
from flask import Flask, render_template, request, redirect, Blueprint

main = Blueprint('main', __name__)
app = Flask(__name__)


@main.route('/', methods=['GET', 'POST'])
@flask_login.login_required
def index_page():
    if request.method == "GET":
        print("GET request registrada")
        print(request.args)
        if request.args.get("start_added"):
            return render_template('index.html', user=flask_login.current_user.id, start_registered=True)
        if request.args.get("end_added"):
            print("se registró un get con date_started")
            return render_template('index.html', user=flask_login.current_user.id, end_registered=True)
    return render_template('index.html', user=flask_login.current_user.id)


@main.route('/start_period', methods=['POST'])
@flask_login.login_required
def start_period():
    today = date.today()
    date_entered = request.form['period_start']
    print("today:", today)
    print(date_entered)
    return redirect('/?start_added=True')


@main.route('/end_period', methods=['POST'])
@flask_login.login_required
def end_period():
    today = date.today()
    date_entered = request.form['period_end']
    print("today:", today)
    print(date_entered)
    print(request.args)
    return redirect('/?end_added=True')


def unauthorized_handler():
    print("unauthorized, redirecting to login page")
    return redirect('/login')

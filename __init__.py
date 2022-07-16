from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from auth_routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from site_routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app


db.create_all(app=create_app())

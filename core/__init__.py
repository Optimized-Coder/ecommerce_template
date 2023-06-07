from flask import Flask
import os
from .extensions import db, migrate, login_manager
from dotenv import find_dotenv, load_dotenv
from .models import User, Product

load_dotenv(find_dotenv())

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # flask login setup
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .models import admin

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # register blueprints
    from .routes import main_bp, product_bp, auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(auth_bp)

    print(f'App: {app} running')

    return app
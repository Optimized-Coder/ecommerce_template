from flask import Flask
import os
from .extensions import db, migrate
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main_bp, product_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(product_bp)

    print(f'App: {app} running')

    return app
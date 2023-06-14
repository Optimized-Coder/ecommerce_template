from flask import Flask, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Message

import stripe

import os

from .extensions import db, migrate, login_manager, mail
from dotenv import find_dotenv, load_dotenv
from .models import User, Product

load_dotenv(find_dotenv())

def create_app():
    app = Flask(__name__)
    # App Config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # mail config
    app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    
    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    admin = Admin(app)

    stripe.api_key = os.environ.get('STRIPE_API_KEY')

    # stripe session routes
    @app.route('/order-success/', methods=['GET'])
    def order_success():
        session_id = request.args.get('session_id')

        session = stripe.checkout.Session.retrieve(session_id)
        customer_email = session.customer_details.email
        customer_name = session.customer_details.name

        email = customer_email if customer_email else "Unknown"
        name = customer_name if customer_name else "Unknown"

        msg = Message(
            'Order Confirmation',
            sender='admin@store.com',
            recipients=[email]
        )
        msg.body=f'Thanks for your order {name}'
        mail.send(msg)
        print('message sent')
        

        return 'Thanks for your order'

    @app.route('/order-cancelled/', methods=['GET'])
    def order_cancelled():
        return 'order cancelled'

    # flask admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Product, db.session))

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
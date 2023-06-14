from flask import render_template, request, Blueprint
from flask_mail import Message
from ..extensions import mail
import stripe
import os

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


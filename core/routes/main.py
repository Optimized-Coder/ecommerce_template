from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
    return '<h1>Main BP</h1>'

@main.route('/order-success', methods=['GET'])
def order_success():
    return 'order successful'

@main.route('/order-cancelled', methods=['GET'])
def order_cancelled():
    return 'order cancelled'
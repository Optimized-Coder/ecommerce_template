from flask import Blueprint

product = Blueprint('product', __name__, url_prefix='/products')

@product.route('/', methods=['GET'])
def index():
    return '<h1>Products route</h1>'
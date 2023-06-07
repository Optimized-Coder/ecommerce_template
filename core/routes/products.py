from flask import Blueprint

product = Blueprint('product', __name__, url_prefix='/products')

@product.route('/', methods=['GET'])
def get_all_products():
    return '<h1>Products route</h1>'

@product.route('/<int:product_id>/', methods=['GET'])
def get_single_product(product_id):
    return f'<h1>Product id: {product_id}</h1>'

@product.route('/<int:product_id>/create-checkout-session/', methods=['GET', 'POST'])
def create_checkout_session(product_id):
    pass
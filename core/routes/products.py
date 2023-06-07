from flask import Blueprint
import os
import stripe

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/', methods=['GET'])
def get_all_products():
    return '<h1>Products route</h1>'

@products.route('/<int:product_id>/', methods=['GET'])
def get_single_product(product_id):
    return f'<h1>Product id: {product_id}</h1>'

# DOMAIN = 'http://127.0.0.1:5000/'

# stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@products.route('/<int:product_id>/create-checkout-session/', methods=['GET', 'POST'])
def create_checkout_session(product_id):
    pass
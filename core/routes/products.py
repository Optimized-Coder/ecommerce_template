from flask import Blueprint, render_template, request
from ..models import Product
import os
import stripe

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/', methods=['GET'])
def get_all_products():
    sort = request.args.get('sort')

    context = {
        'title': 'Products | Store Name',
        'products': Product.query
        .order_by(sort)
        .all()
    }

    return render_template(
        'products/products.html',
        **context
        )

@products.route('/<int:product_id>/', methods=['GET'])
def get_single_product(product_id):
    return f'<h1>Product id: {product_id}</h1>'

# DOMAIN = 'http://127.0.0.1:5000/'

# stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@products.route('/<int:product_id>/create-checkout-session/', methods=['GET', 'POST'])
def create_checkout_session(product_id):
    pass
from flask import Blueprint, render_template, request, flash, redirect
from flask_mail import Message
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
    product = Product.query.get(product_id)
    context = {
        'title': product.name,
        'product': product
    }
    return render_template(
        'products/product_page.html',
        **context
        )

DOMAIN = 'http://127.0.0.1:5000/'

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@products.route('/<int:id>/create-checkout-session/', methods=['GET', 'POST'])
def create_checkout_session(id):
    product = Product.query.filter_by(id=id).first()
    price_id = product.price_id

    try:
        checkout_session = stripe.checkout.Session.create(
            submit_type='pay',
            billing_address_collection='auto',
            shipping_address_collection={
                'allowed_countries': ['GB']
            },
            line_items=[
                {
                    'price': price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=DOMAIN + 'order-success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=DOMAIN + 'order-cancelled/',
        )
    except Exception as e:
        return str(e)
    flash('Purchase Successful!', 'success')
    return redirect(
        checkout_session.url,
        code=303
    )
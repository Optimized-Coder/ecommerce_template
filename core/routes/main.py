from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
    return '<h1>Main BP</h1>'
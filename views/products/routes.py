from flask import Blueprint, render_template

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def show_products():
    # Здесь вы можете добавить логику для получения списка товаров из базы данных
    # Пример: products = Product.query.all()
    products = []  # Замените это реальными данными
    return render_template('products.html', products=products)

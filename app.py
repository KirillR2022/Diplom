from flask import Flask
from views.home.routes import home_bp
from views.products.routes import products_bp
from views.register.routes import register_bp
from views.profile.routes import profile_bp

app = Flask(__name__)

# Регистрация Blueprint для главной страницы
app.register_blueprint(home_bp)

# Регистрация Blueprint для списка товаров
app.register_blueprint(products_bp)

# Регистрация Blueprint для страницы регистрации
app.register_blueprint(register_bp)

# Регистрация Blueprint для профиля пользователя
app.register_blueprint(profile_bp)

# Конфигурация базы данных и других параметров
app.config.from_object('config')

if __name__ == '__main__':
    app.run(debug=True)

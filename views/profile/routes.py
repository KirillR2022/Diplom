from flask import Blueprint, render_template

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
def user_profile():
    # Здесь вы можете добавить логику для получения информации о профиле пользователя
    # Пример: user = current_user  # предполагается, что у вас есть система аутентификации
    user = {}  # Замените это реальными данными
    return render_template('profile.html', user=user)

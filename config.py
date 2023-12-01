import os

class Config:
    # Ключ секрета для обеспечения безопасности приложения
    SECRET_KEY = 'your_secret_key'

    # Настройки базы данных (если используется)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # SQLite в качестве примера
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Режим отладки
    DEBUG = True

    # Дополнительные настройки, если необходимо

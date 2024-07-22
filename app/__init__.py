from flask import Flask
from .services.vector_db_service import VectorDB
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .routes.chat_routes import chat

    app.register_blueprint(chat, url_prefix='/chat')
    app.vector_db_client = VectorDB()

    return app

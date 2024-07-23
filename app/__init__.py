from flask import Flask
from .services.vector_db_service import VectorDB


def create_app():
    app = Flask(__name__)

    from .routes.chat_routes import chat
    from .routes.vectors_routes import vectors

    app.register_blueprint(chat, url_prefix='/chat')
    app.register_blueprint(vectors, url_prefix='/vectors')
    app.vector_db_client = VectorDB()

    return app

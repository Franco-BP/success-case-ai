from flask import Flask
from flask_cors import CORS
from .config.config import Config

from .src.clients.vector_db_client import VectorDB
from .src.services.vector_db_service import populate_vector_db
from .src.clients.model_client import ModelClient
from .src.clients.google_drive_client import DriveClient


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, support_credentials=False)
    
    from .src.controllers.chat_controller import chat
    from .src.controllers.vectors_controller import vectors

    app.register_blueprint(chat, url_prefix='/chat')
    app.register_blueprint(vectors, url_prefix='/vectors')

    populate_vector_db("success_case")

    return app

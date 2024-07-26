from flask import Flask
from flask_cors import CORS

from .services.vector_db_service import VectorDB
from .services.nlp_service_lemmatization import NLPServiceLemmatization


def create_app():
    app = Flask(__name__)
    CORS(app, support_credentials=False)
    ## ELIMINATE - TESTING PURPOSE
    from .routes.test_routes import test
    
    from .routes.chat_routes import chat
    from .routes.vectors_routes import vectors

    ## ELIMINATE - TESTING PURPOSE
    app.register_blueprint(test, url_prefix='/test')
    app.register_blueprint(chat, url_prefix='/chat')
    app.register_blueprint(vectors, url_prefix='/vectors')

    app.vector_db_client = VectorDB()

    return app

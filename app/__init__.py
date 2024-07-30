import atexit

from flask import Flask
from flask_cors import CORS
from .config.config import Config

from .src.services.vector_db_service import populate_vector_db
from .src.jobs.update_success_cases import update_drive_success_cases
from apscheduler.schedulers.background import BackgroundScheduler


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    scheduler = BackgroundScheduler()
    CORS(app, support_credentials=False)
    
    from .src.controllers.chat_controller import chat

    app.register_blueprint(chat, url_prefix='/chat')

    scheduler.add_job(update_drive_success_cases, 'cron', hour=22, minute=0)
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())

    populate_vector_db("success_case")

    return app

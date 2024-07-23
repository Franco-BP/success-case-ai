from flask import Blueprint, request, current_app
from ..services.vector_db_service import populate_vector_db
from ..services.get_drive import *

chat = Blueprint('chat', __name__)


@chat.route('/message', methods=['POST'])
def get_relational_cases():
    data = request.get_json()
    print(populate_vector_db())
    return {"a": populate_vector_db()}

@chat.route('/getdrive', methods=['GET'])
def get_drive_files():
    return get_drives()

from flask import Blueprint, request, jsonify
from ..services.chat_service import generate_chat

chat = Blueprint('chat', __name__)


@chat.route('/message', methods=['POST'])
def post_message():
    data = request.get_json()

    response = generate_chat(data)
    if response is not None:
        return jsonify(response)
    else:
        return jsonify({'code': 500, 'errorMessage': "Unknown server error"}), 500

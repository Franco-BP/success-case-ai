from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from ..services.chat_service import generate_chat
from ..services.validation_service import validate_chat_post

chat = Blueprint('chat', __name__)


@chat.route('/message', methods=['POST'])
def post_message():
    try:
        data = request.get_json()
        validate_chat_post(data)
        response = generate_chat(data)
        if response is not None:
            return jsonify(response)
        else:
            return jsonify({'code': 500, 'errorMessage': "Unknown server error"}), 500
    except ValidationError as err:
        return jsonify({'code': 400, 'errorMessage': err.messages}), 400


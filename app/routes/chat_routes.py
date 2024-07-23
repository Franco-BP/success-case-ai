from flask import Blueprint, request, current_app, abort, jsonify
from ..services.vector_db_service import query

chat = Blueprint('chat', __name__)


def valid_request_params(res, params):
    for param in params:
        val = res.args.get(param)
        if val is None:
            return False
    return True


@chat.route('/message', methods=['POST'])
def get_relational_cases():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'code': 404, 'message': "Invalid body"}), 400
    return query(data)

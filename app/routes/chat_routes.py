from flask import Blueprint, request, current_app, abort
from ..services.vector_db_service import query

chat = Blueprint('chat', __name__)


def valid_request_params(res, params):
    for param in params:
        val = res.args.get(param)
        if val is None:
            return False
    return True


def valid_request_body(body, params):
    for param in params:
        if param not in body:
            return False
    return True


@chat.route('/message', methods=['POST'])
def get_relational_cases():
    data = request.get_json()
    if not valid_request_body(data, ['text']):
        abort(404)
    return query(data)

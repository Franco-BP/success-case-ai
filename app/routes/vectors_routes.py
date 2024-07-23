from flask import Blueprint, request, current_app, jsonify
from ..services.vector_db_service import populate_vector_db

vectors = Blueprint('vectors', __name__)


@vectors.route('/train/<collection>', methods=['POST'])
def get_relational_cases(collection):
    if collection is not None and populate_vector_db(collection):
        return jsonify({'code': 200, 'message': "Trained success"}), 200
    else:
        return jsonify({'code': 500, 'error': 'invalid collection'}), 500

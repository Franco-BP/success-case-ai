from flask import Blueprint, request, current_app, jsonify
from ..services.vector_db_service import populate_vector_db

vectors = Blueprint('vectors', __name__)


@vectors.route('/train', methods=['PUT'])
def train():
    data = request.get_json()

    if data['collection'] is not None and populate_vector_db(data['collection']):  # TODO: VALIDACIONES
        return jsonify({'code': 200, 'message': "Trained success"}), 200
    else:
        return jsonify({'code': 500, 'errorMessage': 'invalid collection'}), 500

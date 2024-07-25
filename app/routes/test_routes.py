from flask import Blueprint, request, abort, jsonify
from ..services.nlp_service_lemmatization import NLPServiceLemmatization

test = Blueprint('test', __name__)


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

@test.route('/nlp', methods=['POST'])
def get_relational_cases():
    data = request.get_json()
    if not valid_request_body(data, ['text']):
        abort(400)
    
    ## Initialize the NLP for search intent.
    return jsonify({'code': 200, 'message': NLPServiceLemmatization().is_search(data['text'])}), 200
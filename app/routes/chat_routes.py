from flask import Blueprint, request, jsonify
from ..services.vector_db_service import query
from ..services.nlp_service_lemmatization import NLPServiceLemmatization

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
        return jsonify({'code': 400, 'message': "Invalid body"}), 400
    
    ## Get NLPService Instance for analyzing search intent.
    if (NLPServiceLemmatization().is_search(data['text'])):    
        return query(data)
    else:
        """
        CHANGE
        """
        ## Call Ollama for a chatbot response.
        return query(data)

from ..models.requests_models import HistorySchema, ChatSchema

history_schema = HistorySchema()
chat_schema = ChatSchema()


def validate_chat_post(request: dict):
    chat_schema.load(request)

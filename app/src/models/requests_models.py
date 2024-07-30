from marshmallow import Schema, fields


class HistorySchema(Schema):
    role = fields.Str(required=True)
    parts = fields.List(fields.Str, required=True)


class ChatSchema(Schema):
    text = fields.Str(required=True)
    history = fields.List(fields.Nested(HistorySchema), required=False)

from typing import Tuple, List, Any

import chromadb


class VectorDB:
    client = None

    def __init__(self):
        if VectorDB.client is None:
            VectorDB.client = chromadb.Client()

    @staticmethod
    def get_or_create_collection(name: str):
        client = VectorDB.client
        target_collection = client.get_or_create_collection(name)
        return target_collection


def map_to_vector_data(data: list) -> tuple[list[Any], list[Any], list[Any]]:
    text_content = []
    ids = []
    metadata = []

    for entry in data:
        text_content.append(entry['presentationText'])
        ids.append(entry['id'])
        metadata.append(entry['metadata'])

    return text_content, ids, metadata


def populate_vector_db():
    collection = VectorDB.get_or_create_collection("success_cases")

    presentations = [{
        "presentationText": "texto",
        "metadata": {
            "title": "titulo.."
        },
        "id": "id"
    }, {
        "presentationText": "texto.....",
        "metadata": {
            "title": "titulo.."
        },
        "id": "id1"
    }]

    parsed_data = map_to_vector_data(presentations)

    collection.upsert(parsed_data)
    return collection

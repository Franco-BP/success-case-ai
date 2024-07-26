from typing import Any
from ..services.get_drive import *
import logging

import chromadb

logger = logging.getLogger(__name__)


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

    @staticmethod
    def get_collection(name: str):
        client = VectorDB.client
        target_collection = client.get_collection(name)
        return target_collection


def map_to_vector_data(data: list) -> dict[str, list[Any]]:
    text_content = []
    ids = []
    metadata = []

    for entry in data:
        text_content.append(entry['presentationText'])
        ids.append(entry['id'])
        metadata.append(entry['metadata'])

    return {
        "documents": text_content,
        "ids": ids,
        "metadata": metadata
    }


def populate_vector_db(collection: str) -> bool:
    try:
        collection = VectorDB.get_or_create_collection(collection)

        presentations = get_drives()

        parsed_data = map_to_vector_data(presentations)

        collection.upsert(
            ids=parsed_data['ids'],
            documents=parsed_data['documents'],
            metadatas=parsed_data['metadata']
        )
        return True
    except Exception as e:
        logger.error(e)
        return False


def query(data, collection="success_case"):
    try:
        default_limit = 2
        collection = VectorDB.get_collection(collection)
        query_result = collection.query(
            query_texts=[data['text']],
            n_results=default_limit
        )
        return query_result
    except Exception as e:
        logger.error(e)
        return None

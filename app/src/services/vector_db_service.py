from typing import Any
from ..services.drive_service import *
from ..clients.vector_db_client import VectorDB
import logging


logger = logging.getLogger(__name__)


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
        collection = VectorDB().get_or_create_collection(collection)

        presentations = get_slides_content()

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
        collection = VectorDB().get_collection(collection)
        query_result = collection.query(
            query_texts=[data['text']],
            n_results=default_limit
        )
        return {
            "documents": query_result['documents'][0],
            "metadatas": query_result['metadatas'][0],
            "ids": query_result['ids'][0],
            "distances": query_result['distances'][0]
        }
    except Exception as e:
        logger.error(e)
        return None

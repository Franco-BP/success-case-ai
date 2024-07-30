import chromadb
import logging

logger = logging.getLogger(__name__)


class VectorDB:
    client = None
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(VectorDB, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            try:
                self.client = chromadb.Client()
                logger.info("Initialized chromaDB client")
            except Exception as e:
                logger.error(f"Error initializing chromaDB client. Error: {e}")

    def get_or_create_collection(self, name: str):
        client = self.client
        target_collection = client.get_or_create_collection(name)
        return target_collection

    def get_collection(self, name: str):
        client = self.client
        target_collection = client.get_collection(name)
        return target_collection

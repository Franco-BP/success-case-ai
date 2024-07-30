import logging
from datetime import datetime
from ..services.vector_db_service import populate_vector_db

logger = logging.getLogger(__name__)


def update_drive_success_cases():
    try:
        populate_vector_db("success_case")
        logger.info(f"update_drive_success_cases executed at {datetime.now()}")
    except Exception as e:
        logger.error(f"update_drive_success_cases executed with errors at {datetime.now()}. Error: {e}")


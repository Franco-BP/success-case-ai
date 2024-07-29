from google.oauth2 import service_account
from googleapiclient.discovery import build
import logging

logger = logging.getLogger(__name__)


class DriveClient:
    drive_service = None
    slide_service = None
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DriveClient, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            try:
                SERVICE_ACCOUNT_FILE = './app/config/service-account-cred.json'
                SCOPES = ['https://www.googleapis.com/auth/drive']
                credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
                self.drive_service = build('drive', 'v3', credentials=credentials)
                self.slide_service = build('slides', 'v1', credentials=credentials)
                logger.info("Initialized google drive client")
            except Exception as e:
                logger.error(f"Error initializing google drive client. Error: {e}")

    def list_drive_files(self, query: str):
        service = self.drive_service
        files = service.files().list(q=query).execute()
        return files

    def get_presentation(self, presentation_id: str):
        service = self.slide_service
        presentation = service.presentations().get(presentationId=presentation_id).execute()
        return presentation

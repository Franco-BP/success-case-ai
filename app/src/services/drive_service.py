import logging

from ..clients.google_drive_client import DriveClient

logger = logging.getLogger(__name__)


def get_file_text(presentation_id):
    presentation = DriveClient().get_presentation(presentation_id)
    slides = presentation.get('slides', [])
    text_content = ""
    for slide in slides:
        for element in slide.get('pageElements', []):
            if 'shape' in element:
                shape = element['shape']
                if 'text' in shape:
                    text_elements = shape['text']['textElements']

                    for text in text_elements:
                        if 'textRun' in text:
                            text_content += '\n' + text['textRun']['content']
    return text_content


def get_slides_content(drive_folder_id: str = '16HFZXMEj86lxImMnzVg-3TL6VsBjQ5gk'):
    query = f"'{drive_folder_id}' in parents"
    results = DriveClient().list_drive_files(query)
    items = results.get('files', [])
    if not items or len(items) == 0:
        logger.warning(f'No files found for folder if {drive_folder_id}')
    else:
        google_docs = []
        for item in items:
            file_data = {
                'presentationText': get_file_text(item['id']),
                'metadata': {
                    'title': item['name']
                },
                'id': item['id']
            }
            google_docs.append(file_data)
        return google_docs

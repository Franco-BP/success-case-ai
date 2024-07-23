from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = './app/config/service-account-cred.json'
# SERVICE_ACCOUNT_FILE = '/config/service-account-cred.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

def get_file_text(presentation_id):
    slides_service = build('slides', 'v1', credentials=credentials)
    presentation = slides_service.presentations().get(presentationId=presentation_id).execute()
    slides = presentation.get('slides', [])
    text_content = ""
    for slide in slides:
        for element in slide.get('pageElements', []):
            if 'shape' in element:
                shape = element['shape']
                if 'text' in shape:
                    text_elements = shape['text']['textElements']
                    for element in text_elements:
                        if 'textRun' in element:
                            text_content += '\n' + f'{element['textRun']['content']}'
    return text_content

def get_drives():
    folder_id = '16HFZXMEj86lxImMnzVg-3TL6VsBjQ5gk'
    query = f"'{folder_id}' in parents"
    results = service.files().list(q=query).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
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
        


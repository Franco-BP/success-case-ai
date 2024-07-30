# Main Specifications:

- Python: v3.12
- Flask: v3.0.3

# For Setting up...

#### 1. Set up Google Drive Credentials:

Link: [Developers Google Drive API](https://developers.google.com/drive/api/quickstart/python?hl=es-419)

#### 2. Add credentials.json
The app consumes the credentials.json from the path: success-case-ai > app > config

`$ cd success-case-ai/app`\
`$ mkdir config`\
`$ touch ./config/credentials.json`

Copy your credentials in this .json file.

#### 3. Copy Google Drive folder id:

The app consumes the Google Slides files from a folder. Open this folder in Google Drive (web) and copy the ID from the web link as showed below:

If this is the link `https://drive.google.com/drive/folders/16HFZXMEj86lxImMnzVg-3TL6VsBjQ5gk`\
This is the ID `16HFZXMEj86lxImMnzVg-3TL6VsBjQ5gk`

#### 4. Insert Google Drive folder id:

The "get_slides_content" function from the "drive_service.py" file located in "success-case-ai > app > src > services" receives the drive folder ID as a parameter. Change the default parameter or the function call to use the desired Folder ID (the one extracted in step 3).

#### 5. Set up Gemini API

#### 6. Add .env for Gemini API

The app consumes the key for Gemini from the path: success-case-ai > app > config

`$ cd success-case-ai/app`\
`$ mkdir config`\
`$ touch ./config/.env`

Copy your key in this .env file.

# For Executing...

### Set up the Virtual Environment:

#### 1. Create the virtual environment

`$ cd success-case-ai`

`$ python3 -m venv .venv`

#### 2. Run the virtual environment.

`$ . .venv/bin/activate`

#### 3. Install the dependencies for the virtual environment.

Use the 'pip' command that suits you

`$ pip3 install -r requirements.txt`

`$ pip install -r requirements.txt`

### Run the Application:

Standing on the success-case-ai folder:

`$ flask --app run run`

# For Developing...

### Install a new dependency:

#### IMPORTANT:
All dependencies not installed locally will be overwritten. Need to have ALL dependencies in the current requirements.txt already installed. If dubious, use an alternate name for 'requirements.txt' name and copy manually the new values.

#### 1. Install the dependency 'test1'

Use the 'pip' command that suits you:

`$ pip3 install test1`

`$ pip install test1`

#### 2. Populate the requirements.txt

Use the 'pip' command that suits you:

`$ pip3 freeze > requirements.txt`

`$ pip freeze > requirements.txt`

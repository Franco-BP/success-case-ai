## Set up the Virtual Environment:

### 1. Create the virtual environment

`$ cd myproject`

`$ python3 -m venv .venv`

### 2. Run the virtual environment.

`$ . .venv/bin/activate`

### 3. Install the dependencies for the virtual environment.
#### Use the 'pip' command that suits you

`$ pip3 install -r requirements.txt`

`$ pip install -r requirements.txt`


## Install a new dependency:

### IMPORTANT:
All dependencies not installed locally will be overwritten. Need to have ALL dependencies in the current requirements.txt already installed. If dubious, use an alternate name for 'requirements.txt' name and copy manually the new values.

### 1. Install the dependency 'test1'
#### Use the 'pip' command that suits you

`$ pip3 install test1`

`$ pip install test1`

### 2. Populate the requirements.txt

`$ pip3 freeze > requirements.txt`

`$ pip freeze > requirements.txt`


## Run the Application:

`flask --app hello run`
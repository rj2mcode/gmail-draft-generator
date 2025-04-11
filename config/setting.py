import os
# General Setting
APP_NAME = "Email Sender Gmail Api"
DEBUG = True


# Paths
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#DATA_DIR = os.path.join(BASE_DIR, "data")
AUTH_DIR = "auth/"
DATA_DIR = "data/"
FUNCTIONS_DIR = "functions/"
ATTACHMENT_DIR = "attachment/"
LOGS_DIR = "logs/"

#Parameters
MAIL_SENDER = 'rj2mcode@gmail.com'
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
CSV_FILE_NAME = 'data.csv'
ATTACHMENT_FILE_NAME = 'attach.txt'
TOKEN_FILE_NAME = 'token.json' #created automatically after running code 
CLIENT_SECRET_FILE = 'client_secret_3822075591-uliofdd.apps.googleusercontent.com.json' # get from google api
SLEEP_TIMER = 10 #Seconds


CSV_FULL_PATH = os.path.join(DATA_DIR, CSV_FILE_NAME)
ATTACHMENT_FULL_PATH = os.path.join(ATTACHMENT_DIR, ATTACHMENT_FILE_NAME)
TOKEN_FULL_PATH = os.path.join(AUTH_DIR, TOKEN_FILE_NAME)
CLIENT_SECRET_FILE_FULL_PATH = os.path.join(AUTH_DIR, CLIENT_SECRET_FILE)

EMAIL_SUBJECT = 'This is your subject '
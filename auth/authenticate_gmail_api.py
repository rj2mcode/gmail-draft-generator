import os
import sys
from config.setting import TOKEN_FULL_PATH,CLIENT_SECRET_FILE_FULL_PATH

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# ----------------------- Google Authentication for Gmail API -----------------------
def authenticate_gmail_api(SCOPES):
    creds = None
    try:
        if os.path.exists(TOKEN_FULL_PATH):
            creds = Credentials.from_authorized_user_file(TOKEN_FULL_PATH, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CLIENT_SECRET_FILE_FULL_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(TOKEN_FULL_PATH, 'w') as token:
                token.write(creds.to_json())
        service = build('gmail', 'v1', credentials=creds)
        return service
    except Exception as error:
        print(f"❌ Authentication Field! : {error}")
        sys.exit(0)



from config.setting import SCOPES,MAIL_SENDER
from auth.authenticate_gmail_api import authenticate_gmail_api
from functions.process_csv_and_send_emails import process_csv_and_send_emails


# ----------------------- Running Program -----------------------
def main():
    service = authenticate_gmail_api(SCOPES)
    sender = MAIL_SENDER
    process_csv_and_send_emails(service, sender)

if __name__ == '__main__':
    main()

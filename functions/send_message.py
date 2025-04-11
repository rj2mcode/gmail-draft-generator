import base64
from .create_message_with_attachment import create_message_with_attachment

def send_message(service, sender, to, subject, body, file_path):
    if not to:
        print(f"❌ No recipient email provided, skipping message.")
        return
    try:
        mime_message = create_message_with_attachment(sender, to, subject, body, file_path)
        raw = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
        draft_body = {'message': {'raw': raw}}
        draft = service.users().drafts().create(userId='me', body=draft_body).execute()
        print(f"📄 Draft created for {to} (draft id: {draft['id']})")
        status = {"status":True,"draft_id":draft['id']}
        return status
    except Exception as error:
        print(f"❌ Error creating draft for {to}: {error}")
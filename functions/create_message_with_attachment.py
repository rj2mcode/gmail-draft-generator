from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import mimetypes
import os

def create_message_with_attachment(sender, to, subject, body, file_path):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg_body = MIMEText(body, 'html')
    message.attach(msg_body)

    content_type, encoding = mimetypes.guess_type(file_path)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)

    with open(file_path, 'rb') as f:
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(f.read())
        encoders.encode_base64(msg)
        msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
        message.attach(msg)

    return message
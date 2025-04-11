import csv
import time
from config.setting import  ATTACHMENT_FULL_PATH,CSV_FULL_PATH,SLEEP_TIMER, EMAIL_SUBJECT
from .send_message import send_message
from .email_body import email_body

def process_csv_and_send_emails(service, sender):
    try:
        with open(CSV_FULL_PATH, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        emails_sent = 0

        with open(CSV_FULL_PATH, mode='r+', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            file.seek(0)

            for row in rows:
                if row['is_send'].lower() == 'yes':
                    continue

                to_email = row['email']
                if not to_email:
                    row['is_send'] = 'no'
                    print(f"❌ No email for {row['fname']} {row['lname']}, skipping.")
                    update_csv(file,fieldnames, rows)
                    continue

                first_name = row['fname']
                last_name = row['lname']
                company_name = row['company']
                subject = f"{EMAIL_SUBJECT} {company_name[:20]}"

                body = email_body(first_name, last_name)

                send_message_status = send_message(service, sender, to_email, subject, body, ATTACHMENT_FULL_PATH)
                if(send_message_status["status"]):
                    row['is_send'] = 'yes'
                    row['draft_id'] = send_message_status["draft_id"]
                    emails_sent += 1
                    print(f"📂 Row updated for {row['fname']} {row['lname']}, marking as 'sent'.")

                    
                    print(f"✅ Data saved for {row['fname']} {row['lname']}")
                    print(f"⏳ Waiting for {SLEEP_TIMER} seconds before next draft...")
                    update_csv(file,fieldnames, rows)
                    time.sleep(SLEEP_TIMER) #seconds

        if emails_sent == 0:
            print("✅ No new drafts created (all done).")
        else:
            print(f"✅ All drafts created successfully. {emails_sent} total.")
    except Exception as error:
        print(f"❌ Error:  {error}")


def update_csv(file, fieldnames, rows ):
    file.seek(0)
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
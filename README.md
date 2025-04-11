# 📧 Gmail Draft Generator with CSV & Attachments

This Python-based project allows you to generate Gmail drafts in bulk using data from a CSV file. It leverages the Gmail API and supports email attachments.

## 🚀 About the Project

The main features of this tool:

- Uses **Google Gmail API** to access your Gmail account.
- Reads a list of emails and content from a **CSV file**.
- Automatically **creates a draft** email for each row in the CSV.
- Supports **file attachments**.
- Handy for sending personalized emails in bulk or preparing them ahead of time.

## 🔧 Requirements & Setup

To run this project, you need to set up a Gmail API project in Google Cloud Console.

### Step-by-step:

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the **Gmail API** for your project.
4. Configure **OAuth 2.0 consent screen** and download the credentials (`credentials.json` file).
5. Place the `credentials.json` file in the root of your project.

### 📦 Install Dependencies

This project uses a few Google API libraries. You can install them using pip:

```bash
pip install --upgrade google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2

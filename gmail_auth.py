from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path
import base64
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from read_files import ReadFiles


class Gmail:
    @staticmethod
    def credentials():
        creds = None
        SCOPES = ['https://mail.google.com/', "https://www.googleapis.com/auth/gmail.send"]
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES
                )
                creds = flow.run_local_server(port=0)
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

        return creds


    def send_message(self, email):
        gm = Gmail()
        creds = gm.credentials()
        try:
            service = build('gmail', 'v1', credentials=creds)
            message = EmailMessage()
            message.set_content('''
                   This is an automated email from the python script made by mohammed nasser
               ''')

            message['To'] = email
            message['From'] = ''
            message['Subject'] = 'Automated Message'

            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            create_message = {
                'raw': encoded_message
            }
            send_message = (service.users().messages().send(userId='me', body=create_message).execute())
        except HttpError as error:
            print(error)
            send_message = None
        return send_message

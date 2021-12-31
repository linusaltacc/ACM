import pickle
import os.path
from webbrowser import get
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/contacts','https://www.googleapis.com/auth/gmail.readonly']

def get_service():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('people', 'v1', credentials=creds)
    return service    
def create_contacts(service,details):
    # CREATING CONTACTS
    name,phone,email,url = details
    service.people().createContact( body={
        "names": [
            {
                "givenName": str(name)
            }
        ],
        "phoneNumbers": [
            {
                'value': phone
            }
        ],
        "emailAddresses": [
            {
                'value': email
            }
        ],
        "urls":[
            {
                'value':url
            }
        ]
    }).execute()
service = get_service()




from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

# Define the scopes your application needs
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Path to your OAuth JSON file (replace with your file path)
CLIENT_SECRET_FILE = os.path.join(base_path, '..', 'data', 'secret.json')
TOKEN_FILE = 'token.pickle'

def get_credentials():
    creds = None
    # Load existing token if available
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as token:
            creds = pickle.load(token)
    # If no valid credentials, start OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=8080)  # Fissa la porta a 8080
        # Save the credentials for next time
        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)
    return creds

# Retrieve credentials and use them to call an API
creds = get_credentials()
print("Access Token:", creds.token)

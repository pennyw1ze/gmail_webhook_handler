import requests
from google.auth.transport.requests import Request
import pickle
import os

# Sender list
# You can use this list if you are interested in checking the sender of the email
# Just add the email address of the sender you want to track in the list (lower case)
senders = []

def get_latest_email():

    # Base path
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Token path
    token_path = os.path.join(base_path, '..', 'data', 'token.pickle')

    # Load OAuth credentials
    with open(token_path, "rb") as token:
        creds = pickle.load(token)

    # Refresh token if expired
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(token_path, "wb") as token:
            pickle.dump(creds, token)

    # Get access token
    access_token = creds.token
    headers = {"Authorization": f"Bearer {access_token}"}

    # Fetch Gmail history based on latest historyId
    latest_message_url = "https://www.googleapis.com/gmail/v1/users/me/messages?maxResults=1"

    # Get the latest message id
    response = requests.get(latest_message_url, headers=headers)
    latest_message_data = response.json()
    message_id = latest_message_data["messages"][0]["id"]

    # Get the latest email by message id
    email_url = f"https://www.googleapis.com/gmail/v1/users/me/messages/{message_id}"
    email_response = requests.get(email_url, headers=headers)
    email_data = email_response.json()

    # Check if the message is "UNREAD"
    if "UNREAD" in email_data["labelIds"]:

        # Extract sender, subject, and snippet
        headers_list = email_data["payload"]["headers"]
        sender = next(h["value"] for h in headers_list if h["name"] == "From")
        subject = next(h["value"] for h in headers_list if h["name"] == "Subject")
        snippet = email_data.get("snippet", "")

        # Debug print
        print(f"Latest Unread Email Received:")
        print(f"Sender: {sender}")
        print(f"Subject: {subject}")
        print(f"Snippet: {snippet}")
        
        # Mark the message as "READ"
        modify_url = f"https://www.googleapis.com/gmail/v1/users/me/messages/{message_id}/modify"
        modify_body = {
            "removeLabelIds": ["UNREAD"]
        }
        requests.post(modify_url, headers=headers, json=modify_body)
    else:
        print("No new unread emails found.")

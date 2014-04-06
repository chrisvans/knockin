# Django
from django.core.exceptions import ImproperlyConfigured

# Third Party
from twilio.rest import TwilioRestClient

# Python
import os

def send_message(message):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    if not account_sid or not auth_token:
        raise ImproperlyConfigured("""
            There was no TWILIO_ACCOUNT_SID or TWILIO_AUTH_TOKEN found in the environment variables. \n
            Please set these variables.
            """)

    client = TwilioRestClient(account_sid, auth_token)
     
    message = client.messages.create(
        to="+16179812689", 
        from_="+16175002819",
        body=message
    )
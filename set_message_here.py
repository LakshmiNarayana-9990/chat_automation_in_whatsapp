from twilio.rest import Client
import os
account_sid = 'your a/c sid'
auth_token = 'your auth token'
client = Client(account_sid, auth_token)
def msg():
    client.messages.create(body='Hello!',from_='whatsapp:+14155238886',to='whatsapp:+91xxxx')

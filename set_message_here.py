from twilio.rest import Client
import os
account_sid = 'AC535a650a257021988975c8a86cb4da55'
auth_token = '05654fb9f5538ef54a2eacfa707c0ddc'
client = Client(account_sid, auth_token)
def msg():
    client.messages.create(body='Hello!',from_='whatsapp:+14155238886',to='whatsapp:+917396237303')
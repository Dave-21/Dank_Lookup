import os
from twilio.rest import Client

#account
account_sid = 'ACd6bfc918599912df528fb96162ecaf70'
auth_token = '9f1c93b28f2e1a972662cb23eb3b74f3'
client = Client(account_sid, auth_token)

#message
message = client.messages.create(
    body="Skrrt",
    from_='+12244006065',
    to='+19062338015'
    )
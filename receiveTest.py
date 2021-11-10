from flask import Flask, request
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse


app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    messageBody = request.form['Body']

    resp = MessagingResponse()
    resp.message('Message from {} -{}'.format(number, messageBody))

    return str(resp)

if __name__ == '__main__':
    app.run()
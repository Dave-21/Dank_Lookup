import requests
from bs4 import BeautifulSoup
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    # number = request.form['From']
    messageBody = request.form['Body']

    URL = "https://www.urbandictionary.com/define.php?term=" + str(messageBody)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="meaning")

    resp = MessagingResponse()
    resp.message('\n{} - {}'.format(messageBody, results.text))

    return str(resp)

if __name__ == '__main__':
    app.run()
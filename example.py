import json
import os

from flask import Flask, request

from courier.app import Messenger, MessengerRequest
from courier.widgets import Message, MessageWidget, Button, PostbackButton
from courier.templates import ButtonTemplate

bot = Messenger('EAAQgCWtPC68BABx8GsqZBwaASskv8fIpOZCcpZAN5pMmB1yihCLY3HHm3nt4HZCzTGZBFZAJ5E8bvttELSqIZCP8kM3I0pAn7gxShQRRzPpGj7oA0mbKzT1188hq0prcBoG8QWfHC6WZAIzQnfl4gyBwMZAlXhzh4H5xfmOmhErnGhwZDZD')

app = Flask(__name__)

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():

    if request.method == 'GET':
        return request.args.get('hub.challenge', 'Get')

    if request.method == 'POST':
        data  = json.loads(request.data.decode('utf-8'))

        entry = data['entry'][0]['messaging'][0]
        fbid    = entry['sender']['id']

        # bot.send(Message(fbid, 'Hello dunia.'))

        try:

            home_buttons  = [PostbackButton('Home', payload='home_button'), PostbackButton('Exit', payload='exit_button')]
            home_template = ButtonTemplate(text='Habari Dunia', buttons=home_buttons)

            code, text = bot.send(MessageWidget(fbid, home_template))
            print(code, text)
        except Exception as ex:
            print(ex)
        finally:
            return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)






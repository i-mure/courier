import json
import os

from flask import Flask, request

from courier.app import Messenger
from courier.widgets import Message, Button
from courier.templates import ButtonTemplate

bot = Messenger(os.environ.get('FB_TOKEN'))

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

        home_buttons  = [Button('postback', 'Home', payload='home_button'), Button('postback', 'Exit', payload='exit_button')]
        home_template = ButtonTemplate(text='Habari Dunia', buttons=home_buttons)

        code, text = bot.send(Message(fbid, home_template))
        print(code, text)
        
        return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)






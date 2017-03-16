import json
from flask import Flask, request

from courier.app import Messenger
from courier.widgets import Message

bot = Messenger(token='<token_here>')
app = Flask(__name__)

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():

    if request.method == 'GET':
        return request.args.get('hub.challenge', 'Get')

    if request.method == 'POST':
        data  = json.loads(request.data.decode('utf-8'))

        entry = data['entry'][0]['messaging'][0]
        fbid    = entry['sender']['id']

        bot.send(Message(fbid, 'Hello dunia.'))

        return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)

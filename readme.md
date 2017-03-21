# Courier

## A library for interacting with Facebook Messenger

### Install courier from pip 

`pip install pycourier`


```python


from courier import Messenger`
bot = Messenger(os.environ.get('FB_TOKEN')) #put facebook token here`

from courier.widgets import Message

bot.send(Message(fbid, 'Hello Dunia'))

```
## License

MIT © [Isaiah Mureithi]

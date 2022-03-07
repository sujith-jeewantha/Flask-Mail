from distutils.log import debug
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sender@gmail.com'
app.config['MAIL_PASSWORD'] = '****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender = 'sender@gmail.com', recipients = ['****@gmail.com'])
    msg.body = "Hello Flask! This message is send from Flask Mail"
    mail.send(msg)
    return 'Message Sent'

if __name__ == '__main__':
    app.run(debug=True)
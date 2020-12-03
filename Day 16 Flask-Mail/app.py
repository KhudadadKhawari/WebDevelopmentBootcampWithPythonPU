from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'example@example.com' #change it 
app.config['MAIL_PASSWORD'] = 'yourPasswordHERE' #your email password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 

@app.route('/')
def index():
    msg = Message('Testing my App',recipients=['khudadad.khawari@gmail.com'],sender='seferyak@gmail.com')
    msg.body="""
            This is just sent for testing the web app
            sorry to disturb you
            best regards
            khudadad khawari 
    """
    mail.send(msg)
    return "Email Sent Successfully!"

if __name__ == "__main__":
    app.run(debug=True)
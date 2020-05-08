import json
import time

from flask import Flask, render_template, url_for, redirect
from flask_oidc import OpenIDConnect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ~ Databases ~ #
db = SQLAlchemy()   #<-Initialize database object
migrate = Migrate() #<-Initialize migration object

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'OIDC_CLIENT_SECRETS': './client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_SCOPES': ["openid", "profile", "email"],
    'OIDC_CALLBACK_ROUTE': '/authorization-code/callback'
})

oidc = OpenIDConnect(app)

# Pull from config file
application.config.from_object('config.Config')

# Initailize database
db.init_app(application)          #<- This will get called in our models.py file
migrate.init_app(application, db) #<- Migration directory

@app.route("/")
def home():
    return "Hello!  There's not much to see here." \
           "Please grab one of our front-end samples for use with this sample resource server"


@app.route("/api/messages")
@oidc.accept_token(True)
def messages():
    response = {
        'messages': [
            {
                'date': time.time(),
                'text': 'I am a robot.'
            },
            {
                'date': time.time()-3600,
                'text': 'Hello, World!'
            }
        ]
    }

    return json.dumps(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

# ~ Import database schemas ~ # 
from app import models

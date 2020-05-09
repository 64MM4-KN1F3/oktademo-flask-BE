import json
import time

from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_oidc import OpenIDConnect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# ~ Databases ~ #
db = SQLAlchemy()   #<-Initialize database object
migrate = Migrate() #<-Initialize migration object

def create_app():
    application = Flask(__name__)
    ma = Marshmallow(application)

    # Pull from config file
    application.config.from_object('config.Config')

    oidc = OpenIDConnect(application)


    # Initailize database
    db.init_app(application)          #<- This will get called in our models.py file
    migrate.init_app(application, db) #<- Migration directory

    @application.route("/")
    def home():
        return "Hello!  There's not much to see here." \
               "Please grab one of our front-end samples for use with this sample resource server"


    @application.route("/api/messages")
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

    if __name__ == 'app':
        application.run(host="0.0.0.0", port=80, debug=True)
    return(application)

# ~ Import database schemas ~ # 
from app import models

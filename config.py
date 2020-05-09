# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# File Name: config.py  
# 
# Sets sqlalchemy uri variable to value specified in .env
#  file
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import os
from dotenv import load_dotenv

# Absolute directory path
basedir = os.path.abspath(os.path.dirname(__file__))

# Looks for and loads .env file
# Can access env variables using os.environ.get(<VARNAME>)
load_dotenv(os.path.join(basedir, '.env'))

# ~ Create config object ~ #
class Config(object):
    # ~~ Migration Repository ~~ #
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'SomethingNotEntirelySecret'
    OIDC_CLIENT_SECRETS = './client_secrets.json'
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    OIDC_SCOPES = ["openid", "profile", "email"]
    OIDC_CALLBACK_ROUTE = '/authorization-code/callback'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# File Name: models.py  
# 
# Creates sql tables for use by flask
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# ~ App specific modules ~ #
from app import db

# ~ Datetime Module ~ #
from datetime import datetime

class testDB(db.Model):
    """testDB extends db.Model class, or creates a database from 
        db.Model class


       Columns
         user_id  : this will equate to 20 char Okta id string
         wellbeing   : a zero to 1 float representation of user wellbeing
         snap_time    : datetime of wellbeing snapshot

    """

    # ~~ String Column ~~ #
    #
    # This is the primary key of the database
    # It is of type = string with max characters = 140
    user_id = db.Column(db.String(32),primary_key=True)

    # ~~ Integer Column ~~ #
    wellbeing = db.Column(db.Float)

    # ~~ Date Column ~~ #
    snap_time = db.Column(db.DateTime, default=datetime.utcnow)
    

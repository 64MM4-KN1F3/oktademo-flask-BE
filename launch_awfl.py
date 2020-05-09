# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# File Name: flask_backend_with_aws.py  
# 
# Script to call from command line to launch application
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from app import create_app 

# ~~~ Create application ~~~ #
application = create_app()

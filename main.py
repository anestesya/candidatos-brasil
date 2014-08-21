# -*- coding: utf-8 -*-
from secrets import SESSION_KEY

from webapp2 import WSGIApplication


import os
import sys
from app.load_csvs import LoadCSVs

csvs = LoadCSVs()
INIDONEOS = csvs.inidoneos
INABILITADOS = csvs.inabilitados

# Third party libraries path must be fixed before importing webapp2
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from app.routes import routes

# webapp2 config
app_config = {
    'webapp2_extras.sessions': {
        'cookie_name': '_simpleauth_sess',
        'secret_key': SESSION_KEY
    },
    'webapp2_extras.auth': {
        'user_attributes': []
    }
}
    
app = WSGIApplication(routes, config=app_config, debug=True)
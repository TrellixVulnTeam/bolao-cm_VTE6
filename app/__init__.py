# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RK'

from app import views

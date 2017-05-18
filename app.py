import os
import sys
from flask import Flask


app = Flask('__name__')
# app.debug = True

sys.path.insert(0, 'models')
sys.path.insert(0, 'db')

from routes import *

if __name__ == '__main__':
    app.secret_key = os.environ.get('SECRET_KEY', 'napoleon')
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', '5000'))
    app.run(HOST, PORT)

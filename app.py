import os
from flask import Flask

app = Flask('__name__')
app.debug = True

from routes import *

if __name__ == '__main__':
    app.secret_key = os.environ.get('SECRET_KEY', 'napoleon')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = int(os.environ.get('SERVER_PORT', '3000'))
    app.run(HOST, PORT)

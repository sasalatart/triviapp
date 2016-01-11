import os
from flask import Flask

app = Flask('__name__')
app.debug = True

from routes import *

if __name__ == '__main__':
    exec(open("./seed.py").read())
    app.secret_key = os.environ.get('SECRET_KEY', 'napoleon')
    SERVER_HOST = os.environ.get('SERVER_HOST', 'localhost')
    SERVER_PORT = int(os.environ.get('SERVER_PORT', '3000'))
    app.run(SERVER_HOST, SERVER_PORT)

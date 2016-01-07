import os
from flask import Flask

app = Flask('__name__')
app.debug = True

from routes import *

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = int(os.environ.get('SERVER_PORT', '5555'))
    app.run(HOST, PORT)

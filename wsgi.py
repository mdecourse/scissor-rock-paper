# adapted from: https://github.com/prof-rossetti/web-app-starter-flask/blob/master/web_app/__init__.py

import os
from flask import Flask
import ssl

# even on localhost still use https to access
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('localhost.crt', 'localhost.key')

from routes import game_routes


app = Flask(__name__)
app.secret_key = 'A0Zr9@8j/3yX R~XHH!jmN]LWX/,?R@T'
app.register_blueprint(game_routes)

app.run(host="127.0.0.1", port="5000", debug=True, ssl_context=context)


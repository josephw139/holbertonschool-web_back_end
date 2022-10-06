#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """ config class for languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ renders index template """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

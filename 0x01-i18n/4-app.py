#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ config class for languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ determine best match for supported languages """
    if request.args.get('locale'):
        if request.args.get('locale') in app.config['LANGUAGES']:
            return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ renders index template """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config():
    """ config class for languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """ call the get_user function """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ determine best match for supported languages """
    if request.args.get('locale'):
        if request.args.get('locale') in app.config['LANGUAGES']:
            return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ checks if user is in database """
    user = request.args.get('login_as')
    try:
        return users.get(int(user))
    except Exception:
        return None


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ renders index template """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

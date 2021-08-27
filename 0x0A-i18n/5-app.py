#!/usr/bin/env python3
"""Basic Babel setup"""


from flask import Flask, g, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)

babel = Babel(app)


class Config:
    """Configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.before_request
def before_request():
    """Identify if user is logged and locale"""
    id_login = request.args.get('login_as')


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Get status API"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """Get local from request"""
    opt_param = request.args.get("locale")
    if opt_param:
        return opt_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> dict:
    """Mock logging in"""
    if id_login in users:
        return users
    return None

if __name__ == "__main__":
    app.run(debug=True)

#!/usr/bin/env python3
"""Basic Babel setup"""


from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config(object):
    """Configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """Get status API"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """Get local from request"""
    opt_param = request.args.get("locale")
    if opt_param in app.config['LANGUAGES']:
        return opt_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)

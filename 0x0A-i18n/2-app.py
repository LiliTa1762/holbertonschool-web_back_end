#!/usr/bin/env python3
"""Basic Babel setup"""


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    """Configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """Get local from request"""
    return request.accept_languages.best_match(app.config['LANGUAGE'])

@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Get status API"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)

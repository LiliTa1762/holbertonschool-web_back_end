#!/usr/bin/env python3
"""Babel basics"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """Get status API"""
    return render_template('templates/0-index.html')


if __name__ == "__main__":
    app.run(debug=True)

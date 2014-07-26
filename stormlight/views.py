

from flask import render_template

from . import app


@app.route('/')
def homepage():
    """Homepage of Stormlight Forum."""
    return render_template('index.html')

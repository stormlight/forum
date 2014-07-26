

from flask import render_template

from . import users


@users.route('/')
def list():
    """List of all people, spren, parshmen and other individuals."""
    return render_template('users.html')

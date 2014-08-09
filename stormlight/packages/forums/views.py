

from flask import render_template, url_for, redirect

from stormlight import pg

from . import forums
from .models import Forum
from .forms import ForumForm


@forums.route('/')
@forums.route('/<id>')
def list(id=None):
    """List of available topics.
    """
    forum = Forum.query.get(id) if id else None

    fora = Forum.query.filter_by(parent=forum).all()
    return render_template('list.html', forum=forum, fora=fora)


# @forums.route('/<id>/create/')
@forums.route('/create/')
def create(id=None):
    """View used to create new forum
    """
    form = ForumForm()

    return render_template('forum.html', form=form)

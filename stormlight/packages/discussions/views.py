

from . import discussions
from .models import Post
from .forms import PostForm
from flask import render_template, url_for, redirect
from stormlight import pg


@discussions.route('reply/<parent_id>', methods=['GET', 'POST'])
def reply(parent_id=None):
    form = PostForm()
    form.parent_id.data = parent_id
    if form.validate_on_submit():
        parent = Post.query.get(form.parent_id.data)
        reply = Post(form.title.data, form.text.data, parent)
        with pg.summon() as session:
            session.add(reply)

        return redirect(url_for('discussion.list'))
    return render_template('reply.html', form=form)

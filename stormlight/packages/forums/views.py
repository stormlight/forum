

from flask import render_template, url_for, redirect, flash

from stormlight import pg

from . import forums
from .models import Forum
from .forms import ForumForm


@forums.route('/')
@forums.route('/<id>')
def list(id=None):
    """List of available topics.
    """
    forum = Forum.query.get_or_404(id) if id else None

    fora = Forum.query.filter_by(parent=forum).all()
    return render_template('forums_list.html', forum=forum, fora=fora)


@forums.route('/<id>/create', methods=['GET', 'POST'])
@forums.route('/create/', methods=['GET', 'POST'])
def create(id=None):
    """View used to create new forum
    """
    if id:
        Forum.query.get_or_404(id)
    return process_form('forums_create.html', ForumForm(), Forum(parent_id=id),
                        msg='New forum was created successfully')


@forums.route('/<id>/update', methods=['GET', 'POST'])
def update(id=None):
    """View used to update existing forum
    """
    forum = Forum.query.get_or_404(id)
    form = ForumForm(obj=forum)
    return process_form('forums_update.html', form, obj=forum,
                        msg='Forum was updated successfully')


@forums.route('/<id>/delete', methods=['POST'])
def delete(id=None):
    """View used to delete existing forum
    """
    forum = Forum.query.get_or_404(id)
    parent_id = forum.parent_id
    with pg.summon() as session:
        session.delete(forum)
    flash("Forum successfully deleted")

    if parent_id:
        return redirect(url_for('.list', id=parent_id))
    else:
        return redirect(url_for('.list'))


def process_form(template, form, obj=None, msg="Operation was successful"):
    if form.validate_on_submit():
        obj = obj or Forum()
        form.populate_obj(obj)
        with pg.summon() as session:
            session.add(obj)
        flash(msg)
        return redirect(url_for('.list', id=obj.id))
    return render_template(template, form=form, forum=obj)

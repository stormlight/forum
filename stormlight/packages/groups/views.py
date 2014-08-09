

from flask import render_template, redirect, url_for

from . import groups
from .models import Group
from .forms import CreateForm
from stormlight import pg


@groups.route('/')
def list():
    """List of all groups"""
    groups = Group.query
    return render_template('groups_list.html', groups=groups)


@groups.route('/create', methods=['GET', 'POST'])
def create():
    """Create new group page."""
    form = CreateForm()
    if form.validate_on_submit():
        group = Group(
            name=form.name.data, 
            description=form.description.data
        )
        with pg.summon() as session:
            session.add(group)
        return redirect(url_for('groups.list'))
    return render_template('groups_create.html', form=form)
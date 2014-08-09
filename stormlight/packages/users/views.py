

from flask import render_template, redirect, url_for

from stormlight.packages.groups.models import Group
from stormlight import pg

from . import users
from .models import User
from .forms import SignupForm


@users.route('/')
def list():
    """List of all people, spren, parshmen and other individuals."""
    users = User.query
    return render_template('users_list.html', users=users)

@users.route('/<id>')
def view(id):
    """View a user"""
    user = User.query.get(id)
    return render_template('users_view.html', user=user)


@users.route('/signup', methods=['GET', 'POST'])
def signup():
    """Sign up page."""
    form = SignupForm()
    if form.validate_on_submit():
        group = Group.query.filter(Group.name == 'Member').first()
        user = User(
            username=form.username.data, 
            email=form.email.data, 
            password=form.password.data, 
            group=group
        )
        with pg.summon() as session:
            session.add(user)
        return redirect(url_for('homepage'))
    return render_template('users_signup.html', form=form)

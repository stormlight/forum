

from stormlight import pg


class User(pg.Model):
    """Representation of a user."""

    id = pg.Column(pg.Integer, primary_key=True)

    #: User's nickname.
    username = pg.Column(pg.String(63), nullable=False)

    #: User's email address.
    email = pg.Column(pg.String(63), nullable=False)

    #: User's password.
    password = pg.Column(pg.String(63), nullable=False)

    #: User's group.
    group_id = pg.Column(pg.Integer, pg.ForeignKey('group.id'))
    group = pg.relationship('Group', uselist=False)

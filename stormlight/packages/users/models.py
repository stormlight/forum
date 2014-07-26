

from stormlight import pg


class User(pg.Model):
    """Representation of a user."""

    id = pg.Column(pg.Integer, primary_key=True)

    #: User's nickname.
    username = pg.Column(pg.String(63), nullable=False)

    #: User's email address.
    email = pg.Column(pg.String(63), nullable=False)

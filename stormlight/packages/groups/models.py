

from stormlight import pg


class Group(pg.Model):
    """Representation of a group."""

    id = pg.Column(pg.Integer, primary_key=True)

    #: Group's name
    name = pg.Column(pg.String(63), nullable=False)

    #: Group's description
    description = pg.Column(pg.String(255), nullable=False)

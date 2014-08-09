

from stormlight import pg


class Forum(pg.Model):

    """Representation of forum"""

    id = pg.Column(pg.Integer, primary_key=True)

    title = pg.Column(pg.String(50), nullable=False)

    description = pg.Column(pg.String(255))

    parent_id = pg.Column(pg.Integer, pg.ForeignKey(id))

    subfora = pg.relationship('Forum', cascade='all', lazy='dynamic',
                              backref=pg.backref('parent', remote_side=id))

    container = pg.Column(pg.Boolean, nullable=False)

    discussions = pg.relationship('Post', cascade='all', lazy='dynamic',
                                  backref=pg.backref('forum', remote_side=id))

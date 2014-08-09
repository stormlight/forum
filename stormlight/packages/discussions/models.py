

from stormlight import pg


class Post(pg.Model):
    """Representation of discussion post."""

    id = pg.Column(pg.Integer, primary_key=True)

    title = pg.Column(pg.String(50), nullable=False)

    text = pg.Column(pg.Text, nullable=False)

    parent_id = pg.Column(pg.Integer, pg.ForeignKey(id))

    replies = pg.relationship(
        'Post',
        cascade='all',
        lazy='dynamic',
        backref=pg.backref('parent', remote_side=id)
    )

    forum_id = pg.Column(pg.Integer, pg.ForeignKey('forum.id'))

    def __init__(self, title, text, parent=None):
        self.title = title
        self.text = text
        self.parent = parent

    def __repr__(self):
        return 'Post(title={}, id={}, parent_id={})'.format(self.title,
                                                            self.id,
                                                            self.parent_id)

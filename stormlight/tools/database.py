
"""
Database Setup
==============

"""

from contextlib import contextmanager

from flask.ext.sqlalchemy import SQLAlchemy as FlaskSQLAlchemy


class SQLAlchemy(FlaskSQLAlchemy):
    """Extention of the original class
    :class:`~flask.ext.sqlalchemy.SQLAlchemy`.
    """

    def __init__(self, app=None):
        with app.app_context():
            super(SQLAlchemy, self).__init__(app)

    def init_app(self, app):
        super(SQLAlchemy, self).init_app(app)

    @contextmanager
    def summon(self):
        """Summons SQLAlchemy's session and commints the transaction
        on the contextmanager's exit. If SQLAlchemy raisesf an error,
        the exception is caught and the transaction rolled back.
        """
        try:
            yield self.session
            self.session.commit()
        except:
            self.session.rollback()
            raise

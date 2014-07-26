# -*- coding: utf-8 -*-


from stormlight import app, pg

from flask.ext.script import Manager, Server
from alembic.config import main as alembic_script


manager = Manager(app)
manager.add_command('runserver', Server())


pg_manager = Manager()


@pg_manager.command
def create():
    """Creates all PostgreSQL tables.

    .. code-block:: bash

        $ python manage.py pg create

    """
    pg.create_all()


@pg_manager.command
def drop():
    """Drops all PostgreSQL tables.

    .. warning::
        Use this command wisely! The droped data is unlikely to be restored.

    .. code-block:: bash

        $ python manage.py pg drop

    """
    if not app.debug:
        raise RuntimeError('Application is not in debug mode.')
    pg.drop_all()


@pg_manager.command
def upgrade():
    """Upgrades the database schema.

    .. code-block:: bash

        $ python manage.py pg upgrade

    """
    alembic_script(argv=('upgrade', 'head'))


@pg_manager.command
def migrate(message='Database migration.'):
    """Runs alembic script to autogenerate migration script.

    .. code-block:: bash

        $ python manage.py pg migrate -m "Updated user table."

    """
    alembic_script(argv=('revision', '--autogenerate', '-m', message))


manager.add_command('pg', pg_manager)


if __name__ == '__main__':
    manager.run()

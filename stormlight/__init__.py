

#: Version number. Consists of three digits:
#:
#: 1.  Major version number of Stormligth forum.
#: 2.  Minor version number, actual version of this app.
#:     Zero should indicate it can change in any moment.
#: 3.  Micro version number.
__version__ = '0.0.1'
__authors__ = ['Pavel Dedík', 'Václav Dedík', 'Jakub Čecháček']


from flask import Flask
from celery import Celery

from .tools import imptools, logutils
from .tools.database import SQLAlchemy


__all__ = ('app', 'pg', 'celery')


# Flask WSGI app setup

app = Flask(__name__)
app.config.from_object('stormlight.settings')
app.config.from_envvar('STORMLIGHT_SETTINGS', silent=False)


# Storage setup

pg = SQLAlchemy(app)


# Celery setup (distributed task queue)

celery = Celery(__name__)
celery.add_defaults(app.config)


# Logging setup

logutils.init_app(app)


# Import all packages

import views  # noqa
import packages

disabled = app.config.get('DISABLED_PACKAGES')
submodules = ['views', 'models', 'tasks']

for module, name in imptools.import_submodules(packages, ignore=disabled):
    modules = imptools.import_submodules(module, submodules)
    if hasattr(module, name):
        app.register_blueprint(getattr(module, name))

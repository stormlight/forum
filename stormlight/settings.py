# -*- coding: utf-8 -*-

"""
Settings
========

"""

import logging


#: Debug flag.
DEBUG = False

#: Logging level.
LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO

#: Logging format.
LOG_FORMAT = '[%(asctime)s: %(levelname)s/%(processName)s] %(message)s'

#: Whether to log connecting to database or not.
LOG_DB_CONNECTIONS = False

#: Redis connection.
REDIS_DATABASE_URI = 'redis://'

#: Redis prefix for keys.
REDIS_PREFIX = '_stormlight'

#: SQLAlchemy connection.
SQLALCHEMY_DATABASE_URI = None

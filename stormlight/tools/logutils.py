
"""
Logging Setup
=============

"""

import logging


def init_app(app):
    """Initialization of all logging stuff.

    :param app: Application object.
    :type app: :class:`flask.Flask`
    """
    # basic configuration
    logging.basicConfig(level=app.config['LOG_LEVEL'],
                        format=app.config['LOG_FORMAT'])

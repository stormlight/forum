# -*- coding: utf-8 -*-


import logging


DEBUG = True

LOG_LEVEL = logging.DEBUG


class conn(object):
    database = 'forum'
    username = 'username'
    password = 'password'
    hostname = 'localhost'


SQLALCHEMY_DATABASE_URI = ('postgresql+psycopg2://{0.username}:{0.password}'
                           '@{0.hostname}/{0.database}').format(conn)

import os

from serversecrets import *



STATIC_PATH = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), 'www2'))
print 'Serving from ' + STATIC_PATH

SQLALCHEMY_DATABASE_URI = 'sqlite:///hippo.db'
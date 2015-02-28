import os

from serversecrets import *

STATIC_PATH = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), 'www'))

print STATIC_PATH
import sys

sys.path.insert(0, "/var/www/wsgi-scripts/")

from app import app

application = app

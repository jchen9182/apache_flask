#!/usr/bin/python3
import sys

sys.path.insert(0,"/var/www/apache_flask/")
sys.path.insert(0,"/var/www/apache_flask/apache_flask/")

import logging
logging.basicConfig(stream=sys.stderr)

from test import app as application


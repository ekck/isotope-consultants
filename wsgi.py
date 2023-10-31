import os
import sys

path = '~/Documents/apps/isotope-consultants'
if path not in sys.path:
    sys.path.append(path)

os.environ['FLASK_CONFIG'] = 'production'
os.environ['SECRET_KEY'] = 'YOUR_SECRET_KEY'
os.environ['SQLALCHEMY_DATABASE_URI'] = ''
os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'] = "False"

from run import app as application

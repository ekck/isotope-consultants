import os
import sys

# config.py

path = ''
if path not in sys.path:
    sys.path.append(path)

os.environ['FLASK_CONFIG'] = 'production'
os.environ['SECRET_KEY'] = 'YOUR_SECRET_KEY'
os.environ['SQLALCHEMY_DATABASE_URI'] = ''




class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}




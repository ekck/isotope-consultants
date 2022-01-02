# config.py

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
    SECRET_KEY = 'shsa123!@#%^'
    SQLALCHEMY_DATABASE_URI = 'postgresql://yzldypyauhqwui:f0a1f63ee99be2f22b5eb8cd90e52296a50dfa31cd959d882052ef4a15948a6d@ec2-3-212-172-25.compute-1.amazonaws.com:5432/d14u68modr0s26'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
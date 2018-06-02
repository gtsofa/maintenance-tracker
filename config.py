# config/config.py
import os

class Config(object):
    """
    Class that contains the configurations objects
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

class DevelopementConfig(Config):
    """
    Class that contains the development configurations
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Contains the Testing configurations
    """
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """
    Contains the Staging configurations
    """
    DEBUG = True

class ProductionConfig(Config):
    """
    Contains the Production configurations
    """
    DEBUG = False
    TESTING = False

app_config = {
    'development':DevelopementConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'production':ProductionConfig
}
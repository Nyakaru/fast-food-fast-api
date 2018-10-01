import os

class Config(object):
    """ Parent configuration class """
    DEBUG = False 
    CSRF_ENABLED = True 
    SECRET_KEY = os.getenv('SECRET_KEY')
    POSTGRES_DATABASE_URI = os.getenv('DB_URL')
    

class DevelopmentConfig(Config):
    """ Development configuration class that inherits from the Config Parent Class"""
    DEBUG = True

class TestConfig(Config):
    """ Testing configuration class that inherits from the Config Parent Class"""
    Testing = True
    DEBUG = True
    POSTGRES_DATABASE_URI = os.getenv('TEST_DATABASE_URL')

class ProductionConfig(Config):
    """ Prduction configuration class that inherits from the Config Parent Class"""
    DEBUG = False
    TESTING = False

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestConfig,
    'production' : ProductionConfig
}





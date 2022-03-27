from os import environ
import datetime
"""
==========================================================================
 ➠ Sweet Taste Backend (https://github.com/RodrigoSiliunas/sweet-taste-flask)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Configurations API
==========================================================================
"""
class Config:
    JSON_SORT_KEYS = False
    THREADED = False
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=2)


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    JWT_SECRET_KEY = environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {
        'DB': environ.get('MONGO_DB_NAME'),
        'HOST': environ.get('MONGO_URI')
    }
    DEBUG = False
    TESTING = False
    THREADED = True


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    JWT_SECRET_KEY = 'THIS IS A SECRET'
    MONGODB_SETTINGS = {
        'DB': 'sweet',
        'HOST': 'mongodb://localhost:27017/sweet'
    }
    DEBUG = True
    TESTING = True
    THREADED = False

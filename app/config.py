from os import environ
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


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    MONGO_URI = environ.get('MONGO_URI')
    DEBUG = False
    TESTING = False
    THREADED = True


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    MONGO_URI = 'mongodb://localhost:27017/'
    DEBUG = True
    TESTING = True
    THREADED = False

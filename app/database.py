from flask_mongoengine import MongoEngine

"""
==========================================================================
 ➠ Sweet Taste Backend (https://github.com/RodrigoSiliunas/sweet-taste-flask)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Database Configuration
==========================================================================
"""

db = MongoEngine()

"""
    Observação:
        Esse arquívo existe para que não ocorra o erro de circular imports.
        Esse código não aceitaria ser criado dentro de __init__.py.
"""
from flask import Flask
from .config import DevelopmentConfig

"""
==========================================================================
 ➠ Sweet Taste Backend (https://github.com/RodrigoSiliunas/sweet-taste-flask)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Core of Aplication (Package)
==========================================================================
"""

app = Flask(__name__)

# Instânciando as configurações da nossa aplicação a partir de uma classe.
app.config.from_object(DevelopmentConfig)

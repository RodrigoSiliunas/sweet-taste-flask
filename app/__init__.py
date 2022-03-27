from flask import Flask
from .database import db
from .config import DevelopmentConfig
from flask_jwt_extended import JWTManager

from .routes.user.index import blueprint as user
from .routes.product.index import blueprint as product

"""
==========================================================================
 ➠ Sweet Taste Backend (https://github.com/RodrigoSiliunas/sweet-taste-flask)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Core of Aplication (Package)
==========================================================================
"""

app = Flask(__name__)
jwt = JWTManager(app)

# Instânciando as configurações da nossa aplicação a partir de uma classe.
app.config.from_object(DevelopmentConfig)

# Aqui instanciamos a database.
db.init_app(app)

# Área de registro de nossas blueprints.
app.register_blueprint(user)
app.register_blueprint(product)

import datetime
from app.database import db
from app.models.Category import Category

"""
==========================================================================
 ➠ Sweet Taste Backend (https://github.com/RodrigoSiliunas/sweet-taste-flask)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Product Model
==========================================================================
"""

class Product(db.Document):
    name = db.StringField(max_length=80, required=True)
    description = db.StringField(max_length=255)
    price = db.FloatField(max_value=1000, required=True)
    category = db.EmbeddedDocumentField(Category)

    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)
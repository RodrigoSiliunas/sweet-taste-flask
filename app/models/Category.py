from app.database import db

"""
==========================================================================
 ➠ Sweet Taste Backend (https://github.com/RodrigoSiliunas/sweet-taste-flask)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Category Model
==========================================================================
"""


class Category(db.EmbeddedDocument):
    name = db.StringField(max_length=64, required=True)
    description = db.StringField(max_length=128, required=True)

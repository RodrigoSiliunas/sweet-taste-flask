from ..database import db

"""
==========================================================================
 ➠ Sweet Taste Backend (https://github.com/RodrigoSiliunas/sweet-taste-flask)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: User
==========================================================================
"""

class User(db.Model):
    name = db.StringField(max_length=60, required=True)
    email = db.StringField(required=True, unique=True)
    birthday = db.DateTimeField(required=True)
    personal_phone = db.StringField(max_length=20)
    personal_celphone = db.StringField(max_length=20, required=True)
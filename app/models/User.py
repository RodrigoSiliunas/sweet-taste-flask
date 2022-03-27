import datetime
from app.database import db

"""
==========================================================================
 ➠ Sweet Taste Backend (https://github.com/RodrigoSiliunas/sweet-taste-flask)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: User Model
==========================================================================
"""


class User(db.Document):
    name = db.StringField(max_length=60, required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(maxlength=32, required=True)
    birthday = db.StringField(required=True)
    personal_phone = db.StringField(max_length=20)
    personal_celphone = db.StringField(max_length=20, required=True)

    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)


"""
    todo:
        user = model_form(User)
        user.password = PasswordField('Password')
"""

from ..database import db

class User(db.Model):
    name = db.StringField(max_length=60, required=True)
    email = db.StringField(required=True, unique=True)
    birthday = db.DateTimeField(required=True)
    personal_phone = db.StringField(max_length=20)
    personal_celphone = db.StringField(max_length=20, required=True)
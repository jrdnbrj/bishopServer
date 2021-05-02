from mongoengine.document import Document
from mongoengine.fields import (
    StringField,
    EmailField,
    DateTimeField
)


class User(Document):
    phone_number = StringField(required=True, unique=True, max_length=15)
    password = StringField(required=True, max_length=20, min_length=8)
    name = StringField(max_length=70)
    nickname = StringField(required=True, max_length=10)
    email = EmailField(max_length=100)
    birth = DateTimeField()
    dni = StringField(unique=True, max_length=13)
    role = StringField()

    meta = {
        'indexes': [{
            'fields': ['dni',],
            'unique': True,
            'partialFilterExpression': {
                'dni': { '$type': 'string' }
            }
        }]
    }
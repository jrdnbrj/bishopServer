from mongoengine.document import Document
from mongoengine.fields import (
    StringField,
    EmailField,
    DateTimeField,
    BooleanField,
    IntField,
    DecimalField
)


class User(Document):
    phone_number = StringField(required=True, unique=True, max_length=15)
    password = StringField(required=True, max_length=20, min_length=6)
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

class Product(Document):
    name = StringField(max_length=60)
    price = DecimalField(precision=2)
    year = StringField(max_length=4)
    transmission = StringField(max_length=2) # AT or MT
    mileage = IntField() # Kilometraje
    color = StringField(max_length=10)
    plate = StringField(unique=True, max_length=7) # Placa
    type = StringField(max_length=20)
    brand = StringField(max_length=30)
    model = StringField(max_length=30)
    registration = DateTimeField()
    cylinder = StringField(max_length=10) # Cilindraje
    country = StringField(max_length=15)
    chassis = StringField(unique=True, max_length=10)
    lien = BooleanField() # Gravamen
    lien_comment = StringField(max_length=200)
    budget = StringField(max_length=10) # Presupuesto - rango
    observation = StringField(max_length=200)
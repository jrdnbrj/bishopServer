from graphene import ObjectType
from graphene import String, Int, Boolean, Date, Decimal


class UserType(ObjectType):
    id = String(required=True)
    phone_number = String(required=True)
    password = String(required=True)
    name = String()
    nickname = String(required=True)
    email = String()
    birth = Date()
    dni = String()
    role = String()

class ProductType(ObjectType):
    id = String(required=True)
    name = String()
    price = Decimal()
    year = String()
    transmission = String() # AT or MT
    mileage = Int() # Kilometraje
    color = String()
    plate = String() # Placa
    type = String()
    brand = String()
    model = String()
    registration = Date()
    cylinder = String() # Cilindraje
    country = String()
    chassis = String()
    lien = Boolean() # Gravamen
    lien_comment = String()
    budget = String() # Presupuesto - rango
    observation = String()

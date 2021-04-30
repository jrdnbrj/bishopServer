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
    name = String(required=True)
    short_name = String()
    price = Decimal()
    description = String()
    picture = String()
    

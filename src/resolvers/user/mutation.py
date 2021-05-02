from graphene import ObjectType, Mutation
from graphene import String, Boolean, Field, Int, Date

from ..type import UserType

from ...services.user_service import create_user


class CreateUser(Mutation):
    class Arguments:
        phone_number = String(required=True)
        password = String(required=True)
        name = String()
        nickname = String(required=True)
        email = String()
        birth = Date()
        dni = String()
        role = String()

    id = String()
    phone_number = String()
    password = String()
    name = String()
    nickname = String()
    email = String()
    birth = Date()
    dni = String()
    role = String()

    def mutate(root, info, phone_number, password, nickname, name=None, email=None, birth=None, dni=None, role=None):
        return create_user(
            phone_number=phone_number, 
            password=password, 
            name=name, 
            nickname=nickname, 
            email=email, 
            birth=birth, 
            dni=dni, 
            role=role
        )


class Mutation(ObjectType):
    create_user = CreateUser.Field()

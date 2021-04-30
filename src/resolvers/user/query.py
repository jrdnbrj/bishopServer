from graphene import ObjectType
from graphene import String, Int, List, Field

from ..type import UserType

import datetime


class Query(ObjectType):
    get_users = List(UserType)
    get_user = Field(UserType, id=String(required=True))

    def resolve_get_users(parent, info):
        return [
            {
                'id': '1',
                'phone_number': "0984790449",
                'password': "123456",
                'name': "Jordan Borja",
                'nickname': "Jordan",
                'email': "elruix@bishop.com",
                'birth': datetime.date(1998, 9, 19),
                'dni': "1717270175",
                'role': "admin",
            },
            {
                'id': '2',
                'phone_number': "0987654321",
                'password': "654321",
                'name': "Todd Henst",
                'nickname': "Todd",
                'email': "todd@bishop.com",
                'birth': "2008-02-25",
            },
        ]

    def resolve_get_user(parent, info, id):
        return {
            'id': id,
            'phone_number': "0984790449",
            'password': "123456",
            'name': "Jordan Borja",
            'nickname': "Jordan",
            'email': "elruix@bishop.com",
            'birth': datetime.date(1998, 9, 19),
            'dni': "1717270175",
            'role': "admin",
        }

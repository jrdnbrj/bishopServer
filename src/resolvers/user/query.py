from graphene import ObjectType
from graphene import String, Int, List, Field

from ..type import UserType

from ...services.user_service import get_all_users, get_one_user 


class Query(ObjectType):
    get_users = List(UserType)
    get_user = Field(UserType, id=String(required=True))

    def resolve_get_users(parent, info):
        return get_all_users()

    def resolve_get_user(parent, info, id):
        return get_one_user(id)
        

from graphene import ObjectType
from graphene import String, Int, List, Field

from ..type import ProductType

from ...services.product_service import get_all_products, get_one_product


class Query(ObjectType):
    get_products = List(ProductType)
    get_product = Field(ProductType, id=String(required=True))

    def resolve_get_products(parent, info):
        return get_all_products()

    def resolve_get_product(parent, info, id):
        return get_one_product(id)
        

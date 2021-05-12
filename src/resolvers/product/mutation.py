from graphene import ObjectType, Mutation
from graphene import String, Boolean, Int, Date, Decimal

from ...services.product_service import create_product


class CreateProduct(Mutation):
    class Arguments:
        name = String()
        price = Decimal()
        year = String()
        transmission = String()
        mileage = Int()
        color = String()
        plate = String()
        type = String()
        brand = String()
        model = String()
        registration = Date()
        cylinder = String()
        country = String()
        chassis = String()
        lien = Boolean()
        lien_comment = String()
        budget = String()
        observation = String()

    id = String()
    name = String()
    price = Decimal()
    year = String()
    transmission = String()
    mileage = Int()
    color = String()
    plate = String()
    type = String()
    brand = String()
    model = String()
    registration = Date()
    cylinder = String()
    country = String()
    chassis = String()
    lien = Boolean()
    lien_comment = String()
    budget = String()
    observation = String()

    def mutate(root, info, name=None, price=None, year=None, transmission=None, 
        mileage=None, color=None, plate=None, type=None, brand=None, model=None, 
        registration=None, cylinder=None, country=None, chassis=None, lien=None, 
        lien_comment=None, budget=None, observation=None):
        return create_product(
            name=name, 
            price=price, 
            year=year, 
            transmission=transmission, 
            mileage=mileage, 
            color=color, 
            plate=plate, 
            type=type,
            brand=brand,
            model=model,
            registration=registration,
            cylinder=cylinder,
            country=country,
            chassis=chassis,
            lien=lien,
            lien_comment=lien_comment,
            budget=budget,
            observation=observation,
        )


class Mutation(ObjectType):
    create_product = CreateProduct.Field()

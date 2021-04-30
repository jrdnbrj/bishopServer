from graphene import ObjectType, Schema

# queries
# from .resolvers.product.query import Query as product_query
from .resolvers.user.query import Query as user_query

# mutations
# from .resolvers.product.mutation import Mutation as product_mutation
from .resolvers.user.mutation import Mutation as user_mutation


# class Query(product_query, user_query, ObjectType): pass
class Query(user_query, ObjectType): pass

# class Mutation(product_mutation, user_mutation, ObjectType): pass
class Mutation(user_mutation, ObjectType): pass


schema = Schema(query=Query, mutation=Mutation)

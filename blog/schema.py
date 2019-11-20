import graphene
import blogger.schema


class Query(blogger.schema.Query, graphene.ObjectType):
    pass


class Mutation(blogger.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

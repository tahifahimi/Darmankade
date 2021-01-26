import graphene
import graphql_jwt

from authentication.graphql import Query as AuthenticationQuery, Mutation as AuthenticationMutation
from main.graphql import Query as MainQuery, Mutation as MainMutation


class Query(AuthenticationQuery, MainQuery, graphene.ObjectType):
    pass


class Mutation(AuthenticationMutation, MainMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

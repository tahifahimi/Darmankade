import graphene as graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphql_jwt.decorators import login_required

from authentication.models import User
from authentication.serializers import UserSerializer


class UserType(DjangoObjectType):
    name = graphene.String()
    type = graphene.String()

    class Meta:
        model = User

    def resolve_name(self, info):
        return self.name

    def resolve_type(self, info):
        return self.type


class UserMutation(SerializerMutation):
    class Meta:
        serializer_class = UserSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class Query(graphene.ObjectType):
    user = graphene.Field(UserType)

    @login_required
    def resolve_user(self, info):
        return info.context.user


class Mutation(graphene.ObjectType):
    user_mutation = UserMutation.Field()

import graphene as graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from graphql_jwt.decorators import login_required

from main.filters import DoctorFilter
from main.models import Doctor, Comment, Spec
from main.serializers import CommentSerializer


class DoctorNode(DjangoObjectType):
    pk = graphene.Int()
    name = graphene.String()
    week_days = graphene.List(graphene.Boolean)

    class Meta:
        model = Doctor
        filterset_class = DoctorFilter
        interfaces = (graphene.relay.Node, )

    def resolve_pk(self, info):
        return self.pk

    def resolve_name(self, info):
        return self.user.name

    def resolve_week_days(self, info):
        return [str(i)[0] in ["T", "t"] for i in list(self.week_days)]


class DoctorType(DjangoObjectType):
    name = graphene.String()
    week_days = graphene.List(graphene.Boolean)

    class Meta:
        model = Doctor

    def resolve_name(self, info):
        return self.user.name

    def resolve_week_days(self, info):
        return [str(i)[0] in ["T", "t"] for i in list(self.week_days)]


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class SpecType(DjangoObjectType):
    class Meta:
        model = Spec


class CommentMutation(SerializerMutation):
    class Meta:
        serializer_class = CommentSerializer
        model_operations = ['create']

    @classmethod
    @login_required
    def mutate(cls, root, info, input):
        return super(CommentMutation, cls).mutate(root, info, input)


class Query(graphene.ObjectType):
    doctors = DjangoFilterConnectionField(DoctorNode)
    doctor = graphene.Field(DoctorType, pk=graphene.Int())
    specs = graphene.List(SpecType)

    def resolve_doctor(self, info, pk):
        return Doctor.objects.get(pk=pk)

    def resolve_specs(self, info):
        return Spec.objects.all()


class Mutation(graphene.ObjectType):
    comment_mutation = CommentMutation.Field()

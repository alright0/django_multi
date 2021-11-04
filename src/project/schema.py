import graphene
from graphene_django.filter import DjangoFilterConnectionField
from books.schema import BookNode, CreateBook, UpdateBook


class Query(graphene.ObjectType):
    name = "Schema"

    book = graphene.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    auto_camelcase=True,
)

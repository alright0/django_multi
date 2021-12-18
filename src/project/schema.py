import graphene
from graphene_django.filter import DjangoFilterConnectionField
from books.schema import BookNode, CreateBook, UpdateBook, DeleteBook
from protocol.schema import (
    CreateProtocol,
    DeleteProtocol,
    ProtocolNode,
    UpdateProtocol,
    ScreenNode,
    CreateScreen,
    DeleteScreen,
    UpdateScreen,
)


class Query(graphene.ObjectType):
    name = "Schema"

    book = graphene.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode)

    protocol = graphene.Node.Field(ProtocolNode)
    protocols = DjangoFilterConnectionField(ProtocolNode)

    screen = graphene.Node.Field(ScreenNode)
    screens = DjangoFilterConnectionField(ScreenNode)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

    create_protocol = CreateProtocol.Field()
    update_protocol = UpdateProtocol.Field()
    delete_protocol = DeleteProtocol.Field()

    create_screen = CreateScreen.Field()
    update_screen = UpdateScreen.Field()
    delete_screen = DeleteScreen.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    auto_camelcase=True,
)

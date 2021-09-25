import graphene
from graphene.relay.node import Node
from graphene_django import DjangoObjectType

from new.models import Book


class BookNode(DjangoObjectType):
    title = graphene.String()
    author = graphene.String()

    class Meta:
        model = Book
        interfaces = (Node,)
        filter_fields = {
            "id": ["exact"],
            "title": ["exact", "icontains"],
            "author": ["exact", "icontains", "in"],
        }

    def resolve_title(self, info, **kwargs):
        return self.title

    def resolve_author(self, info, **kwargs):
        return self.author


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        author = graphene.String()

    book = graphene.Field(BookNode)

    @classmethod
    def mutate(cls, root, info, title, author, id):
        book = Book.objects.get(pk=id)
        book.title = title
        book.author = author
        book.save()

        return UpdateBook(book=book)


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        author = graphene.String()

    book = graphene.Field(BookNode)

    @classmethod
    def mutate(cls, root, info, title, author):
        book = Book()
        book.title = title
        book.author = author
        book.save()

        return CreateBook(book=book)

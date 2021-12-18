import graphene
from graphene.relay.node import Node
from graphene_django import DjangoObjectType
from graphql_relay import from_global_id

from books.models import Book


class BookNode(DjangoObjectType):
    title = graphene.String()
    author = graphene.String()
    category = graphene.String()

    class Meta:
        model = Book
        interfaces = (Node,)
        filter_fields = {
            "id": ["exact"],
            "title": ["exact", "icontains"],
            "author": ["exact", "icontains", "in"],
            "category": ["exact", "icontains"],
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
        category = graphene.String()

    book = graphene.Field(BookNode)

    @classmethod
    def mutate(cls, root, info, title, author, id, category):
        book = Book.objects.get(pk=id)
        book.title = title
        book.author = author
        book.category = category
        book.save()

        return UpdateBook(book=book)


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        author = graphene.String()
        category = graphene.String()

    book = graphene.Field(BookNode)

    @classmethod
    def mutate(cls, root, info, title, author, category):
        book = Book()
        book.title = title
        book.author = author
        book.category = category
        book.save()

        return CreateBook(book=book)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookNode)

    @classmethod
    def mutate(cls, root, info, id):
        _, id = from_global_id(id)
        book = Book.objects.get(pk=id)
        book.delete()

        return DeleteBook(book=book)

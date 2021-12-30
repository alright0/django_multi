import graphene
from graphene.relay.node import Node
from graphene_django import DjangoObjectType
from graphql_relay import from_global_id
from graphene_file_upload.scalars import Upload
from django.core.files import File

from protocol.models import Protocol, Screen


class ProtocolNode(DjangoObjectType):
    title = graphene.String()
    type = graphene.String()

    class Meta:
        model = Protocol
        interfaces = (Node,)
        filter_fields = {
            "title": ["exact"],
            "type": ["exact"],
        }


class UpdateProtocol(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        type = graphene.String()

    protocol = graphene.Field(ProtocolNode)

    @classmethod
    def mutate(cls, root, info, title, id, type):
        _, id = from_global_id(id)
        protocol = Protocol.objects.get(pk=id)
        protocol.title = title
        protocol.type = type
        protocol.save()

        return UpdateProtocol(protocol=protocol)


class CreateProtocol(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        type = graphene.String()

    protocol = graphene.Field(ProtocolNode)

    @classmethod
    def mutate(cls, root, info, title, type):
        protocol = Protocol()
        protocol.title = title
        protocol.type = type
        protocol.save()

        return CreateProtocol(protocol=protocol)


class DeleteProtocol(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    protocol = graphene.Field(ProtocolNode)

    @classmethod
    def mutate(cls, root, info, id):
        _, id = from_global_id(id)
        protocol = Protocol.objects.get(pk=id)
        protocol.delete()

        return DeleteProtocol(protocol=protocol)


class ScreenNode(DjangoObjectType):
    type = graphene.String()
    parent = graphene.String()

    class Meta:
        model = Screen
        interfaces = (Node,)
        filter_fields = {"type": ["exact"], "parent": ["exact"]}


class UpdateScreen(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        type = graphene.String()
        description = graphene.String()
        key = graphene.Float()

    screen = graphene.Field(ScreenNode)

    @classmethod
    def mutate(cls, root, info, title, id, type, description, key):
        screen = Screen.objects.get(pk=id)
        screen.title = title
        screen.type = type
        screen.description = description
        screen.key = key
        screen.save()

        return UpdateScreen(screen=screen)


class CreateScreen(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        type = graphene.String()
        description = graphene.String()
        key = graphene.Float()
        parent = graphene.String()

    screen = graphene.Field(ScreenNode)

    @classmethod
    def mutate(cls, root, info, title, type, description, key, parent):
        _, id = from_global_id(parent)
        parent = Protocol.objects.get(id=id)

        screen = Screen()
        screen.title = title
        screen.type = type
        screen.description = description
        screen.key = key
        screen.parent = parent
        screen.save()

        return CreateScreen(screen=screen)


class DeleteScreen(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    screen = graphene.Field(ScreenNode)

    @classmethod
    def mutate(cls, root, info, id):
        _, id = from_global_id(id)
        screen = Screen.objects.get(pk=id)
        screen.delete()

        return DeleteScreen(screen=screen)

class UploadImage(graphene.Mutation):
    class Arguments:
        image = Upload()
        description = graphene.String()
        parent = graphene.String()
        key = graphene.Float()

    screen = graphene.Field(ScreenNode)

    @classmethod
    def mutate(cls, root, info, image, description, parent, key):
        _, id = from_global_id(parent)
        parent = Protocol.objects.get(id=id)

        screen = Screen()
        screen.image=image
        screen.description= description
        screen.type=Screen.IMAGE_SCREEN
        screen.parent=parent
        screen.key=key
        screen.save()

        return UploadImage(screen=screen)
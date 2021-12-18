from django.contrib import admin
from protocol.models import Protocol, Screen


@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("type", "title", "created")


@admin.register(Screen)
class TextScreenAdmin(admin.ModelAdmin):
    list_display = ("type", "title", "description", "parent", "created")

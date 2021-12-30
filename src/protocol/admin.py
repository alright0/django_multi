from django.contrib import admin
from protocol.models import Protocol, Screen


class TextScreenInline(admin.StackedInline):
    model = Screen
    extra = 0

@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("type", "title", "created")
    inlines = [TextScreenInline]


@admin.register(Screen)
class TextScreenAdmin(admin.ModelAdmin):
    list_display = ("type", "title", "description", "parent", "created")

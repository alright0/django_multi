from django.contrib import admin
from books.models import Book


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category")
    search_fields = ("title", "author", "category")

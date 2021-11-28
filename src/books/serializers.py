from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ("id",)

    def create(self, validated_data):
        author = validated_data.get("author")
        category = validated_data.get("category")
        title = validated_data.get("title")

        object = Book.objects.create(**validated_data)
        return object

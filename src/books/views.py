from rest_framework import serializers, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from books.models import Book
from books.serializers import BookSerializer


class BookView(GenericAPIView):
    serializer_class = BookSerializer
    # authentication_classes = (JWTAuthentication, BasicAuthentication)

    def get(self, request, *args, **kwargs):
        qs = Book.objects.all()

        return Response(qs.values(), status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            response_json = {"message": "ok"}
            return Response(response_json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

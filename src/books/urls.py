from django.urls import path, re_path

from books.views import BookView


urlpatterns = [
    path("book/", BookView.as_view()),
]

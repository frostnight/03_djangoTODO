from django.urls import path
from rest_framework import routers

from .serializers import BooksAPIMixins, BookAPIMixins, BookViewSet
from .views import HelloAPI, booksAPI, bookAPI, BookAPI, BooksAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("fbv/books", booksAPI),
    path("fbv/book/<int:bid>", bookAPI),

    path("cbv/books", BooksAPI.as_view()),
    path("cbv/book/<int:bid>", BookAPI.as_view()),

    path("mixin/books", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>", BookAPIMixins.as_view()),
]

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns.extend(router.urls)

from django.urls import path

from .views import *


urlpatterns = [
    path('books_just', BooksView.as_view())
]

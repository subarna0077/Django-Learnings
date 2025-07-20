from django.urls import path
from . import views

urlpatterns = [
    path("books", views.bookList, name='book-lists'),
    path("books/<str:slug>", views.bookDetails, name='book-details')
]

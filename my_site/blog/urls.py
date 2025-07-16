from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("posts", views.allPosts , name="all-posts"),
    path("posts/<slug:slug>", views.singlePost, name="single-post"),
]

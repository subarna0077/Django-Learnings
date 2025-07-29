from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blog-home'),
    path('blog-admin/', views.admin, name='blog-admin'),
    path('thank_you/', views.thank_you, name='thank-you'),
    path('blogs/<int:id>', views.singleBlog, name='single-blog')


]

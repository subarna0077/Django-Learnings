from django.urls import path
from . import views

urlpatterns = [
    path("", views.feedback_form, name='feedback-form'),
    path("thank_you/",views.thank_you, name='thank-you'),
    path("feedbacks/", views.feedback_list)
]

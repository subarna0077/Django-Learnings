from django.db import models

# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    review = models.TextField()
    accept_terms = models.BooleanField()



from django.db import models
from django.utils.text import slugify

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    rating = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    country= models.CharField(max_length=60)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.country} {self.code}"

    class Meta:
        verbose_name_plural = "Countries Entries"    

    


class Address(models.Model):
    street = models.CharField(max_length = 80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.street} {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"    


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="Books")
    is_bestselling = models.BooleanField(default=False)
    slug= models.SlugField(default="" , blank=True, null=False, db_index=True) 
    published_country = models.ManyToManyField(Country)

    def __str__(self):
        return f"{self.title} ({self.rating})"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()
    

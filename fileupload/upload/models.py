from django.db import models

# Create your models here.

class FileUpload(models.Model):
    title = models.CharField()
    image = models.FileField(upload_to= 'uploads/') 

    def __str__(self):
        return self.title
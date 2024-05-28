from django.db import models
from cloudinary.models import CloudinaryField

class Reviews(models.Model):
    name = models.CharField(max_length = 20)
    review = models.CharField(max_length = 255)
    def __str__(self):
        return self.name

class Galery(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = CloudinaryField('image')
    def __str__(self):
        return self.title


from django.db import models
from cloudinary.models import CloudinaryField

class Reviews(models.Model):
    name = models.CharField(max_length = 20)
    review = models.CharField(max_length = 255)
    rating = models.IntegerField(null=True, blank=True, default = 0)
    image = CloudinaryField('review_image', null=True, blank=True)
    def __str__(self):
        return self.name

class Galery(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = CloudinaryField('image')
    def __str__(self):
        return self.title

class Webcontent(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.heading


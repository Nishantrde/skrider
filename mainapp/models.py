from django.db import models

class Reviews(models.Model):
    name = models.CharField(max_length = 20)
    review = models.CharField(max_length = 255)
    def __str__(self):
        return self.name


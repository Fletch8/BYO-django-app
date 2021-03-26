from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField()

    def __str__(self):
        return "cards model class"
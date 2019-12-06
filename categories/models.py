from django.db import models

class Category(models.Model):
    image = models.ImageField(upload_to='images/')
    headline = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    pass

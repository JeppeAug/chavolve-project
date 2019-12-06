from django.db import models

class Challenge(models.Model):
    image = models.ImageField(upload_to='images/', default='download.jpg')
    headline = models.CharField(max_length=50, default='0000000')
    description = models.CharField(max_length=200, default='0000000')

from django.db import models

# Create your models here.
class burger(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
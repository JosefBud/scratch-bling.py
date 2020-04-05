from django.db import models
from django.contrib.postgres import fields

# Create your models here.


class Item(models.Model):
    item_name = models.TextField()
    item_description = models.TextField()
    item_size = fields.ArrayField(models.TextField())
    item_cost = models.IntegerField()

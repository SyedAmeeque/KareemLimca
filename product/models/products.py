from django.db import models
from .category import Category
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    large_price = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
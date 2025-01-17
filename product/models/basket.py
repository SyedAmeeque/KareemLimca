from django.db import models
from .customer import Customer
from .products import Product 
# Create your models here.
class Basket(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    total_price = models.IntegerField(null=True, blank=True)
    
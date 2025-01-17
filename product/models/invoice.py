from django.db import models
from .basket import Basket
from .Sales_limca import Sales_limca
# Create your models here.
class Invoice(models.Model):
    products = models.ManyToManyField('Sales_limca', related_name='products')
    total_price = models.FloatField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    discount = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    delivery_charges = models.CharField(max_length=50, null=True, blank=True)
    discounted_amount = models.IntegerField(null=True, blank=True)
    paid_or_not = models.BooleanField(default=False)
    recieved_cash = models.IntegerField()
    returned_cash = models.FloatField(default=0)
    delivery_man_name = models.CharField(max_length=50, null=True, blank=True)

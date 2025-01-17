from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, default="customer")
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
    
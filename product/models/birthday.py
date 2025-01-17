from django.db import models

# Create your models here.
class Birthday(models.Model):
    name = models.CharField(max_length=50, default="customer")
    phone = models.CharField(max_length=50, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name
    
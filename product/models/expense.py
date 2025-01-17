from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Generated by Django 5.0.7 on 2024-08-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_invoice_recieved_cash'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='returned_cash',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 5.0.7 on 2024-08-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_invoice_returned_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='returned_cash',
            field=models.FloatField(default=0),
        ),
    ]

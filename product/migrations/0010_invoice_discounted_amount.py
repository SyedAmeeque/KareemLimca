# Generated by Django 5.0.7 on 2024-08-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_invoice_delivery_charges_invoice_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='discounted_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_invoice_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

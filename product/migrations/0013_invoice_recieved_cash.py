# Generated by Django 5.0.7 on 2024-08-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_invoice_paid_or_not'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='recieved_cash',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
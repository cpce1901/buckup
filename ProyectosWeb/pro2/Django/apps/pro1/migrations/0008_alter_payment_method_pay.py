# Generated by Django 4.1.7 on 2023-02-22 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro1', '0007_payment_station_number_station_remove_extras_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='method_pay',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]

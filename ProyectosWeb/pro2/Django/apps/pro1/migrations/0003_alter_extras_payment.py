# Generated by Django 4.1.7 on 2023-02-16 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro1', '0002_station_name_alter_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extras',
            name='payment',
            field=models.CharField(choices=[('1', 'Key'), ('2', 'transitcard'), ('3', 'creditcard'), ('4', 'phone')], max_length=1),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0005_alter_variable_created_alter_variable_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ingresado'),
        ),
    ]
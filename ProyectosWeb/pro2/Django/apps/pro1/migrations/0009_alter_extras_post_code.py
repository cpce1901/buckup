# Generated by Django 4.1.7 on 2023-02-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro1', '0008_alter_payment_method_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extras',
            name='post_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

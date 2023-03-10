# Generated by Django 4.1.7 on 2023-02-22 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro1', '0004_payment_remove_extras_payment_extras_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='network',
            name='company',
        ),
        migrations.RemoveField(
            model_name='network',
            name='location',
        ),
        migrations.RemoveField(
            model_name='network',
            name='station',
        ),
        migrations.RemoveField(
            model_name='extras',
            name='payment',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Network',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AddField(
            model_name='extras',
            name='payment',
            field=models.CharField(choices=[('0', 'key'), ('1', 'transitcard'), ('2', 'creditcard'), ('3', 'phone')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]

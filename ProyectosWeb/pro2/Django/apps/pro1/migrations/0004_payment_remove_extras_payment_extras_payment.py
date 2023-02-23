# Generated by Django 4.1.7 on 2023-02-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro1', '0003_alter_extras_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_payment', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='extras',
            name='payment',
        ),
        migrations.AddField(
            model_name='extras',
            name='payment',
            field=models.ManyToManyField(to='pro1.payment'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-02-23 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bills',
            name='type',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='type',
        ),
        migrations.AddField(
            model_name='bills',
            name='type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='bills.docuemnts'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tickets',
            name='type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='bills.docuemnts'),
            preserve_default=False,
        ),
    ]
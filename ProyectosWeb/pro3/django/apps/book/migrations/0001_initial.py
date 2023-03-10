# Generated by Django 4.1.7 on 2023-02-21 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='nombre')),
                ('fecha', models.DateField(verbose_name='fecha de lanzamiento')),
                ('portada', models.ImageField(upload_to='portada')),
                ('visitas', models.PositiveIntegerField()),
                ('autores', models.ManyToManyField(to='author.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.categoria')),
            ],
        ),
    ]

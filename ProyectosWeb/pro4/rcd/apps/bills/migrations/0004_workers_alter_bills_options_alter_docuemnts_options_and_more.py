# Generated by Django 4.1.7 on 2023-02-23 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_alter_docuemnts_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=20, verbose_name='Apellido')),
                ('position', models.CharField(max_length=30, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
                'ordering': ('id',),
            },
        ),
        migrations.AlterModelOptions(
            name='bills',
            options={'ordering': ('date',), 'verbose_name': 'Factura', 'verbose_name_plural': 'Facturas'},
        ),
        migrations.AlterModelOptions(
            name='docuemnts',
            options={'ordering': ('id',), 'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='tickets',
            options={'ordering': ('date',), 'verbose_name': 'Boleta', 'verbose_name_plural': 'Boletas'},
        ),
        migrations.AlterField(
            model_name='bills',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='giro',
            field=models.CharField(max_length=30, verbose_name='Giro'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bills.docuemnts', verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bills.docuemnts', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='bills',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bills.workers', verbose_name='Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tickets',
            name='user',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='bills.workers', verbose_name='Usuario'),
            preserve_default=False,
        ),
    ]

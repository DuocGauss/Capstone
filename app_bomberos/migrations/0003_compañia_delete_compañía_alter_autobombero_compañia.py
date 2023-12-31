# Generated by Django 4.2.5 on 2023-09-30 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_bomberos', '0002_compañía'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compañia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_compañia', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Compañía',
        ),
        migrations.AlterField(
            model_name='autobombero',
            name='compañia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_bomberos.compañia'),
        ),
    ]

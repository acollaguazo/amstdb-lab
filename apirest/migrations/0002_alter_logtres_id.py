# Generated by Django 3.2.5 on 2021-08-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtres',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

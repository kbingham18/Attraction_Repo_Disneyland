# Generated by Django 2.2 on 2023-12-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_auto_20231206_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='ride_name',
            field=models.CharField(error_messages={'unique': 'This ride already exists'}, max_length=200, unique=True),
        ),
    ]
# Generated by Django 2.2 on 2023-12-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20231118_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]

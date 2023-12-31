# Generated by Django 2.2 on 2023-11-08 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_name', models.CharField(max_length=200)),
                ('ride_desc', models.CharField(max_length=500)),
                ('height_limit', models.CharField(max_length=200)),
                ('ride_location', models.CharField(max_length=200)),
                ('ride_wait', models.CharField(max_length=200)),
                ('ride_image', models.ImageField(default='images/none/noimg.jpg', upload_to='ride_images')),
            ],
        ),
    ]

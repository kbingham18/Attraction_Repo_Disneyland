from django.db import models


# Create your models here.

class Rides(models.Model):

    def __str__(self):
        return self.ride_name

    ride_name = models.CharField(max_length=200)
    ride_desc = models.CharField(max_length=500)
    height_limit = models.CharField(max_length=200)
    ride_location = models.CharField(max_length=200)
    ride_wait = models.CharField(max_length=200)
    ride_image = models.ImageField(upload_to='ride_images', default='images/none/noimg.jpg')

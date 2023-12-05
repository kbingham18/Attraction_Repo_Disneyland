from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class Rides(models.Model):

    def __str__(self):
        return self.ride_name

    ride_name = models.CharField(max_length=200)
    ride_desc = models.CharField(max_length=500)
    height_limit = models.CharField(max_length=200)
    ride_location = models.CharField(max_length=200)
    ride_wait = models.CharField(max_length=200)
    ride_image = models.ImageField(upload_to='ride_images', default='ride_images/default.jpg')


class Review(models.Model):
    reviewer_username = models.CharField(max_length=200)
    reviewed_ride = models.CharField(max_length=200)
    review = models.CharField(max_length=500)
    rating = models.IntegerField()



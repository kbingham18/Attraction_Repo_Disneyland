from django import forms
from .models import Rides, Review
from django.core.files.uploadedfile import SimpleUploadedFile


class RideForm(forms.ModelForm):
    class Meta:
        model = Rides
        fields = ['ride_name', 'ride_desc', 'height_limit', 'ride_location', 'ride_wait', 'ride_image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_username', 'reviewed_ride', 'review', 'rating']



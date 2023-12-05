from django.shortcuts import render
from .models import Rides, Review
from .forms import RideForm, ReviewForm
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect

from django.http import HttpResponse

# Create your views here.

def ride_list(request):
    ride_object = Rides.objects.all()
    ride_name = request.GET.get('ride_name')
    ride_location = request.GET.get('ride_location')
    if ride_name != '' and ride_name is not None:
        ride_object = ride_object.filter(ride_name__icontains=ride_name)
    elif ride_location != '' and ride_location is not None:
        ride_object = ride_object.filter(ride_location__icontains=ride_location)
    paginator = Paginator(ride_object, 10)
    page = request.GET.get('page')
    ride_object = paginator.get_page(page)
    return render(request, 'repository/ride_list.html', {'ride_object': ride_object})


def detail(request, ride_id):
    ride = Rides.objects.get(pk=ride_id)
    reviews = Review.objects.filter(reviewed_ride=ride.ride_name)
    context = {
        'ride': ride,
        'reviews': reviews
    }
    return render(request, 'repository/ride_detail.html', context)


# class RideDetail(DetailView):
#     model = Rides
#     template_name = 'repository/detail.html'

def create_ride(request):
    form = RideForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        # return render(request, 'repository/ride-form.html', {'form': form})
        return redirect('repository:ride_list')
    return render(request, 'repository/ride-form.html', {'form': form})


class CreateRide(CreateView):
    model = Rides
    fields = ['ride_name', 'ride_desc', 'height_limit', 'ride_location', 'ride_wait', 'ride_image']
    template_name = 'repository/ride-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def create_review(request, ride_id):
    ride = Rides.objects.get(pk=ride_id)
    # reviews = Review.objects.filter(reviewed_ride=ride.ride_name)
    # ride = Rides.objects.get(id=ride_id)
    reviewed_ride1 = Rides.objects.get(ride_name=ride.ride_name)
    form = ReviewForm(request.POST or None)
    form.reviewed_ride = reviewed_ride1

    if form.is_valid():
        form.save()
        return redirect('../%s' % ride_id)

    return render(request, 'repository/review-form.html', {'form': form, 'item': reviewed_ride1})

def update_ride(request, ride_id):
    ride = Rides.objects.get(id=ride_id)
    form = RideForm(request.POST or None, request.FILES or None, instance=ride)

    if form.is_valid():
        form.save()
        return redirect('repository:ride_list')

    return render(request, 'repository/ride-form.html', {'form': form, 'item': ride})


def delete_ride(request, ride_id):
    ride = Rides.objects.get(id=ride_id)

    if request.method == 'POST':
        ride.delete()
        return redirect('repository:ride_list')

    return render(request, 'repository/ride-delete.html', {'ride': ride})


def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    ride = Rides.objects.get(ride_name=review.reviewed_ride)

    if request.method == 'POST':
        review.delete()
        return redirect('../%s' % ride.id)
        # return redirect('repository:ride_list')

    return render(request, 'repository/review-delete.html', {'review': review})

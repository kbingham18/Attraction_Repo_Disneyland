from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'repository'
urlpatterns = [
    path('', views.ride_list, name="ride_list"),
    path('<int:ride_id>', views.detail, name="detail"),
    # path('add', views.CreateRide.as_view(), name="create_ride"),
    path('add', views.create_ride, name="create_ride"),
    path('update/<int:ride_id>', views.update_ride, name="update_ride"),
    path('delete/<int:ride_id>', views.delete_ride, name="delete_ride"),
    path('deleteReview/<int:review_id>', views.delete_review, name="delete_review"),
    path('addReview/<int:ride_id>', views.create_review, name="create_review"),
]

urlpatterns += [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
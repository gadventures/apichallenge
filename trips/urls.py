from django.conf.urls import url

from trips import views

urlpatterns = [
    url(r'^trips/$', views.ListTrips())
]

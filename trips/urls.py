from django.conf.urls import url
from trips import views

urlpatterns = [
    url(r'^$', views.trip_list),
    url(r'^(?P<pk>[0-9]+)/$', views.trip_detail)
]

from django.conf.urls import url
from trips import views
from rest_framework.urlpatterns import format_suffix_patterns

""" Define all the views with as_view()"""
trip_list = views.TripList.as_view()
trip_detail = views.TripDetail.as_view()
trip_list_view = views.TripView.as_view()

urlpatterns = [
    url(r'^$',trip_list_view),
    url(r'^(?P<pk>[0-9]+)/$', trip_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trips import views
from .views import TripView

urlpatterns = [
    url('^', TripView.as_view()),
    url(r'^trips/$', views.trip_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.trip_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

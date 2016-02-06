from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TripView, TripViewAPI, TripViewAPIDetail

urlpatterns = [
    url(r'^api/$', TripViewAPI.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/(?P<pk>[0-9]+)/$', TripViewAPIDetail.as_view()),
    url(r'^', TripView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
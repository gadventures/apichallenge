from django.conf.urls import url, include
from trips import views
from .views import TripView, TripList, TripDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^trips-api/$', TripList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^trips-api/(?P<pk>[0-9]+)/$', TripDetail.as_view()),
    url(r'^', TripView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

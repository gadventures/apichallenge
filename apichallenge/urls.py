"""apichallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from trips import models, views


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Trip
        fields = ('name', 'start_date', 'finish_date')

		
class TripViewSet(viewsets.ModelViewSet):
    queryset = models.Trip.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'trips', TripViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^trips/', include('trips.urls')),
	url(r'^api/$', views.trip_list),
	url(r'^api/(?P<pk>[0-9]+)/$', views.trip_detail),
]

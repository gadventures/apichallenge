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
from django.conf.urls import patterns, url, include
from trips import views
from trips.views import TripView
from trips.models import Trip

urlpatterns = [
    
	#To display a full list of current trips being offered we accept the /trips/ portion of the url
    #url(r'^trips/$', views.ListTrips.as_view(), name='trips_list'),
    
    #If a number exists after /trips/ such as /trips/1, we display that particular trip detail
    url(r'^trips/(?P<pk>[0-9]+)/$', views.TripDetail.as_view()),
    
	#Collect the data when /trips/ is typed and format it in a template for user
    url(r'^trips/$', TripView.as_view(
    	queryset = Trip.objects.all(),
    	context_object_name = "trips",
    	template_name='trips/index.html'))
]




from django.views.generic import TemplateView
from trips.models import Trip
from trips.serializers import TripSerializer
from rest_framework import generics
class TripView(TemplateView):
    template_name = 'trips/index.html'

class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

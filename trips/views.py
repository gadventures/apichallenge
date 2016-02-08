from django.views.generic import TemplateView
from rest_framework import generics
from serializers import TripSerializer
from models import Trip

""" Method responsible for /trips/api/ """
class TripViewAPI(generics.ListCreateAPIView):   
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
""" Method responsible for /trips/api/<id>/ """
class TripViewAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
""" Method responsible for the home page """
class TripView(TemplateView):
    template_name = 'trips/index.html'
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework import generics
from serializers import TripSerializer
from models import Trip
import json
from django.http import HttpResponse

class TripViewAPI(generics.ListCreateAPIView):   
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
class TripViewAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
class TripView(TemplateView):
    template_name = 'trips/index.html'
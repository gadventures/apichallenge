from rest_framework.views import APIView
from rest_framework.response import Response
from trips.serializers import TripSerializer
from trips.models import Trip
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic.list import ListView

class ListTrips(ListView):

    def get(self, request, format=None):
        """
        Return a list of all trips. Not being used.
        """
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)
        
class TripDetail(APIView):
    """
    Retrieve a single trip detail. This is an APIView; /lists/1 .. /lists/2 .. 
    """
    def get_trip(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404()

    def get(self, request, pk, format=None):
        trip = self.get_trip(pk)
        trip = TripSerializer(trip)
        return Response(trip.data)

class TripView(ListView):
    """
    Used with the template to show a list of all trips. 
    """
    model = Trip

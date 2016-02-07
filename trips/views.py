from trips.models import Trip
from trips.serializer import TripSerializer
from django.views.generic.list import ListView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class TripList(APIView):
    """
    Retrieve a list of Trips
    """
    def get(self, request, format=None):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

class TripDetail(APIView):
    """
    Retrive a single Trip
    """

    def get_object(self, pk):
        """
        Helper method to check for existing object
        """
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        """
        Http Get method to return a single instance of trip
        """
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)

class TripView(ListView):
    """
    ListView to display Trips on a custom html page
    """
    template_name = 'trips/index.html'
    model = Trip
    def get_context_data(self, **kwargs):
        context = super(TripView, self).get_context_data(**kwargs)
        context['trips'] = Trip.objects.all()
        return context

    

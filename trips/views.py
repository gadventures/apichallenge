from trips.models import Trip
from trips.serializer import TripSerializer
from django.views.generic.list import ListView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.generic.base import TemplateView

class TripList(APIView):
    def get(self, request, format=None):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

class TripDetail(APIView):
    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)

class TripView(ListView):
    template_name = 'trips/index.html'
    model = Trip
    def get_context_data(self, **kwargs):
        context = super(TripView, self).get_context_data(**kwargs)
        context['trips'] = Trip.objects.all()
        return context

    

# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from trips.models import Trip
from trips.serializers import TripSerializer
from django.views.generic import TemplateView

class TripView(TemplateView):
    template_name = 'trips/index.html'

@api_view(['GET'])
def trip_list(request, format=None):
    """
    List all trips.
    """
    if request.method == 'GET':
        trips = Trip.objects.all()
        serializer = TripAPISerializer(trips, many=True)
        return JSONResponse(serializer.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def trip_detail(request, pk, format=None):
    """
    Retrieve a trip instance.
    """
    try:
        trip = Trip.objects.get(pk=pk)
    except Trip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TripSerializer(trip)
        return Response(serializer.data)

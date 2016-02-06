from trips.models import Trip
from trips.serializer import TripSerializer

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
	
@csrf_exempt
def trip_list(request):

    if request.method == 'GET':
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def trip_detail(request, pk):

    try:
        trip = Trip.objects.get(pk=pk)
    except Trip.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TripSerializer(trip)
        return JSONResponse(serializer.data)


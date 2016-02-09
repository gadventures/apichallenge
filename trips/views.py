from django.views.generic import TemplateView
from rest_framework.response import Response
from trips.models import Trip
from trips.serializers import TripSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class TripView(TemplateView):
    template_name = 'trips/index.html'

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
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

    elif request.method == 'POST':        
        data = JSONParser().parse(request)
        trip = Trip.objects.create(name=data['name'], start_date=data['start_date'], finish_date=data['finish_date'])
        trip.save()
        return JSONResponse(data, status=201)    

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        Trip.objects.filter(name=data['name']).delete()
        return HttpResponse(status=204)
		
@csrf_exempt
def trip_detail(request, pk):
    try:
        trip = Trip.objects.get(pk=pk)
    except Trip.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TripSerializer(trip)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TripSerializer(trip, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        trip.delete()
        return HttpResponse(status=204)
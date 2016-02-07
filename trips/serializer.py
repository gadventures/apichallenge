from rest_framework import serializers
from trips.models import Trip

class TripSerializer (serializers.ModelSerializer):
	"""
	Serializer for the Trip Model
	"""
	class Meta:
		model = Trip
		fields = ('pk', 'name', 'start_date', 'finish_date', 'destination')

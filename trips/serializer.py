from rest_framework import serializers
from trips.models import Trip

class TripSerializer (serializers.Serializer):
	pk = serializer.IntegerFrield(read_only=True)
	name = serializer.CharField(required=True, allow_blank=False, max_length=55)
	start_date = serializer.DateField()
	finish_data = serializer.DateField()
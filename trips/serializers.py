from rest_framework import serializers
from trips.models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'name', 'start_date', 'finish_date')

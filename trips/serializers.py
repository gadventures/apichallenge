from rest_framework import serializers
from trips.models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'name', 'start_date', 'finish_date')

    def index(self, validated_data):
        """
        Create and return a new `Trip` instance, given the validated data.
        """
        return Trip.objects.create(**validated_data)

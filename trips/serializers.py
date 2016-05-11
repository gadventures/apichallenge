from rest_framework import serializers
from trips.models import Trip

class TripSerializer(serializers.Serializer):
    name = serializers.CharField()
    start_date = serializers.IntegerField()
    finish_date = serializers.IntegerField()

    def index(self, validated_data):
        """
        Create and return a new `Trip` instance, given the validated data.
        """
        return Trip.objects.create(**validated_data)

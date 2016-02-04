from rest_framework import serializers
from trips.models import Trip

#Serializers are used to format the data into a more readable format for JSON
class TripSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=55)
    start_date = serializers.DateField()
    finish_date = serializers.DateField()
    tour_capacity = serializers.IntegerField()
    package_price = serializers.IntegerField()
    package_location = serializers.CharField(max_length=55)



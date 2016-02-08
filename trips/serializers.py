from rest_framework import routers, serializers, viewsets
from models import Trip

""" Method to serialize one Trip object """
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'name', 'start_date', 'finish_date')
from rest_framework import serializers
from trips.models import Trip


class TripSerializer(serializers.Serializer):
    class Meta:
        model = Trip
        fields = ('name', 'start_date', 'finish_date')
	
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    start_date = serializers.DateField(format=None, input_formats=None)
    finish_date = serializers.DateField(format=None, input_formats=None)

    def create(self, validated_data):
        """
        Create and return a new `Trip` instance, given the validated data.
        """
        return Trip.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Trip` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.finish_date = validated_data.get('finish_date', instance.finish_date)
        instance.save()
        return instance
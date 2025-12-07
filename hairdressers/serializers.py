from rest_framework import serializers
from .models import Hairdresser, Service, Availability

class HairdresserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hairdresser
        fields = '__all__'
        read_only_fields = ['user', 'rating_avg']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'
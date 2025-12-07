from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hairdresser, Service, Availability
from .serializers import HairdresserSerializer, ServiceSerializer, AvailabilitySerializer

class HairdresserViewSet(viewsets.ModelViewSet):
    queryset = Hairdresser.objects.all()
    serializer_class = HairdresserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        hairdresser = Hairdresser.objects.get(user=request.user)
        serializer = self.get_serializer(hairdresser)
        return Response(serializer.data)

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Service.objects.filter(hairdresser__user=self.request.user) if self.request.user.is_authenticated else Service.objects.none()

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Availability.objects.filter(hairdresser__user=self.request.user) if self.request.user.is_authenticated else Availability.objects.none()
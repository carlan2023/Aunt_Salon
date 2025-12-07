from django.shortcuts import render

# Create your views here.
# bookings/views.py
from rest_framework import viewsets, permissions
from django.shortcuts import render
from .models import Booking, Review
from .serializers import BookingSerializer, ReviewSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Hairdressers see only their bookings
        if self.request.user.is_authenticated:
            try:
                hairdresser = self.request.user.hairdresser
                return Booking.objects.filter(hairdresser=hairdresser)
            except:
                pass
        return Booking.objects.none()

    def perform_create(self, serializer):
        serializer.save()


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
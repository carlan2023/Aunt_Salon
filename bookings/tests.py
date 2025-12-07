from django.test import TestCase

# Create your tests here.
from rest_framework import viewsets, permissions
from .models import Booking, Review
from .serializers import BookingSerializer, ReviewSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Booking.objects.filter(hairdresser__user=self.request.user)
        return Booking.objects.none()

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
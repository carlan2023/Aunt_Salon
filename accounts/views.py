from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegisterSerializer, LoginSerializer

def landing_page(request):
    """Landing page for Aunt Salon"""
    return render(request, 'landing.html')

def stylists_page(request):
    """Stylists listing page"""
    return render(request, 'stylists.html')

def services_page(request):
    """Services listing page"""
    return render(request, 'services.html')

def bookings_page(request):
    """Bookings page"""
    return render(request, 'bookings.html')

def register_page(request):
    """Registration page"""
    return render(request, 'register.html')

def login_page(request):
    """Login page"""
    return render(request, 'login.html')

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
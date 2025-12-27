# hairline/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import your views for auth
from accounts.views import (
    RegisterView, LoginView, landing_page, stylists_page, 
    services_page, bookings_page, register_page, login_page
)

# Router for all API endpoints
from rest_framework.routers import DefaultRouter
from hairdressers.views import HairdresserViewSet, ServiceViewSet, AvailabilityViewSet
from bookings.views import BookingViewSet, ReviewViewSet


router = DefaultRouter()
router.register(r'hairdressers', HairdresserViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'availabilities', AvailabilityViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', landing_page, name='landing'),
    path('stylists/', stylists_page, name='stylists'),
    path('services/', services_page, name='services'),
    path('bookings/', bookings_page, name='bookings'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('admin/', admin.site.urls),
    
    # Auth endpoints
    path('api/auth/register/', RegisterView.as_view(), name='api-register'),
    path('api/auth/login/', LoginView.as_view(), name='api-login'),
    
    # API routes
    path('api/', include(router.urls)),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
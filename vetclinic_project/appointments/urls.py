from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', AppointmentViewSet, basename='appointments')

urlpatterns = [path('', include(router.urls))]
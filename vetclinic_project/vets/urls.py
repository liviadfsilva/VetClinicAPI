from rest_framework.routers import DefaultRouter
from .views import VetsViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', VetsViewSet, basename='vets')

urlpatterns = [path('', include(router.urls))]
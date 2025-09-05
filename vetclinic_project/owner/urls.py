from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', OwnerViewSet, basename='owner')

urlpatterns = [path('', include(router.urls))]
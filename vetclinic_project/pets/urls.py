from rest_framework.routers import DefaultRouter
from .views import PetViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', PetViewSet, basename='pet')

urlpatterns = [path('', include(router.urls))]
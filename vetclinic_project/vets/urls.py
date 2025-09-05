from rest_framework.routers import DefaultRouter
from .views import VetsViewSet

router = DefaultRouter()
router.register(r'vets', VetsViewSet, basename='vets')

urlpatterns = router.urls
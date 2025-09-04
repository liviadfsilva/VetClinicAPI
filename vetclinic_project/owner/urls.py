from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet

router = DefaultRouter()
router.register(r'owner', OwnerViewSet, basename='owner')

urlpatterns = router.urls
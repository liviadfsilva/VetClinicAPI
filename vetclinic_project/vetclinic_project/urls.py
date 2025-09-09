from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import LogoutView

schema_view = get_schema_view(
   openapi.Info(
      title="Vet Clinic API",
      default_version='v1',
      description="A Django API created for managing vets, pets, owners, and appointments for a vet clinic.",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pets/', include("pets.urls")),
    path('api/owners/', include("owners.urls")),
    path('api/vets/', include("vets.urls")),
    path('api/appointments/', include("appointments.urls")),
    path('api/users/', include("users.urls")),
    
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

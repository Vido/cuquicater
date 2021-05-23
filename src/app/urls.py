from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from rest_framework import routers
from rest_framework_simplejwt.views import (
     TokenObtainPairView,
     TokenRefreshView,
     TokenVerifyView,
)

from helpers.health_check import health_check
from offer.views import OfferViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'offers', OfferViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Enables the DRF browsable API page
    #path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("health_check/", health_check, name="health_check"),
    #
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]

if settings.ENVIRONMENT == "development":
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

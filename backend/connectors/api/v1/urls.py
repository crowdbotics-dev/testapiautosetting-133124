from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors133124ViewSet

router = DefaultRouter()
router.register(
    "testconnectors133124", Testconnectors133124ViewSet, basename="testconnectors133124"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]

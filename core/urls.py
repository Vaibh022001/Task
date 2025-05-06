from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, UserProjectViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/', UserProjectViewSet.as_view({'get': 'list'})),
]

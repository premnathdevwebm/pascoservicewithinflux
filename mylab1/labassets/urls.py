from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Labassets

router = DefaultRouter()
router.register(r'assets', Labassets, basename='')

urlpatterns = [
        path('assets/model/<str:model_name>/start/', Labassets.as_view({'get': 'startservicepasco'}), name='startsensor'),
        path('assets/model/<str:model_name>/', Labassets.as_view({'get': 'retrieve_by_model'}), name='asset-by-model'),
        path("", include(router.urls)),
]

from django.urls import path
from .views import SpecialistServiceViewSet, BusinessViewSet, ServiceViewSet, SpecialistViewSet

urlpatterns = [
    path('specialist-services/', SpecialistServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='specialist-service-list'),
    path('specialist-services/<int:pk>/', SpecialistServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='specialist-service-detail'),
    path('businesses/', BusinessViewSet.as_view({'get': 'list', 'post': 'create'}), name='business-list'),
    path('businesses/<int:pk>/', BusinessViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='business-detail'),
    path('services/', ServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='service-list'),
    path('services/<int:pk>/', ServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='service-detail'),
    path('specialists/', SpecialistViewSet.as_view({'get': 'list', 'post': 'create'}), name='specialist-list'),
    path('specialists/<int:pk>/', SpecialistViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='specialist-detail'),
]
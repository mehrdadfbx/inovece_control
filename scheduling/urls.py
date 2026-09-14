from django.urls import path
from .views import availabilityViewSet, bookingViewSet

urlpatterns = [
    path('availability/', availabilityViewSet.as_view({'get': 'list', 'post': 'create'}), name='availability-list'),
    path('availability/<int:pk>/', availabilityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='availability-detail'),
    path('booking/', bookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-list'),
    path('booking/<int:pk>/', bookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-detail'),
]
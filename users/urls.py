from django.urls import  path
from .views import OwnerViewSet, CustomerViewSet


urlpatterns = [
    path('owners/', OwnerViewSet.as_view({'get': 'list', 'post': 'create'}), name='owner-list'),
    path('owners/<int:pk>/', OwnerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='owner-detail'),
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
    path('customers/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='customer-detail'),
]
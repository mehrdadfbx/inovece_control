# products/urls.py
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')

urlpatterns = router.urls
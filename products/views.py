from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.permissions import IsAdminRole
from .serializers import CompanySerializer, CategorySerializer, ProductSerializer
from .models import Company, Category, Product


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [IsAdminRole()]
        return [IsAuthenticatedOrReadOnly()]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [IsAdminRole()]
        return [IsAuthenticatedOrReadOnly()]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [IsAdminRole()]
        return [IsAuthenticatedOrReadOnly()]
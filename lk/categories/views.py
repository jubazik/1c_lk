from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ProductsGroup, Products
from .serializers import ProductsSerializers, ProductsGroupSerializers


class ProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [permissions.IsAdminUser]


class ProductsGroupViewset(viewsets.ModelViewSet):
    queryset = ProductsGroup.objects.all()
    serializer_class = ProductsGroupSerializers
    permission_classes = [permissions.IsAdminUser]
# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import CustomUserSerializer
from .models import CustomUser




class CustomUserViews(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets, permissions, exceptions
from .serializers import CustomUserSerializer, ProfileCustomUserSerializer
from .models import CustomUser

from django.contrib.auth import get_user_model


class CustomUserViews(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]


class ProfileCustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProfileCustomUserSerializer
    permission_classes =  [permissions.IsAuthenticated]
# Create your views here.
    def get_queryset(self):
        if self.request.user:
            user = get_user_model().oblejct.filter(pk=self.request.user.pk)
            if user is None:
                raise exceptions.AuthenticationFailed("Пользователь не найден")
            return user
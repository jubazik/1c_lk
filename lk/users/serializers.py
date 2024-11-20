import uuid

from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'full_name', 'status', 'password']
    def create(self, validated_date):
        user = super().create(validated_date)
        user.set_password(validated_date['password'])
        user.save()
        return user



    def update(self, instance, validated_date):
        user = super().update(instance, validated_date)
        try:
            user.set_password(validated_date['password'])
            user.save()
        except KeyError:
            pass
        return user
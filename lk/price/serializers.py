import uuid
from .models import Prices
from rest_framework import serializers


class PricesSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source="product.full_name")

    class Meta:
        model = Prices
        fields = ['id', 'product', 'title', 'price']

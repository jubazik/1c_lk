from django.urls import path, include
from .views import StandartResultSetPagination , PriseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/v1/price', PriseViewSet, basename='price' )

urlpatterns = [
    path('', include(router.urls)),

]
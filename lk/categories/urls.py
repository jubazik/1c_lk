from django.urls import path, include
from .views import ProductsViewset, ProductsGroupViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/v1/products', ProductsViewset, basename='products' )
router.register(r'api/v1/products_group', ProductsGroupViewset, basename='products_group' )

urlpatterns = [
    path('', include(router.urls)),

]
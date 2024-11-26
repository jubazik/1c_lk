from django.db import models
from categories.models import ProductsGroup, Products
# Create your models here.


class Prices(models.Model):
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Наменклатура', related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2,   verbose_name='цена', blank=True, default=0)


    def __str__(self):
        return f'{self.product} : {self.price}'

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'

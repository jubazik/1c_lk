import uuid

from django.db import models


# Create your models here.
class ProductsGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='Наименование', max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Родитель', blank=True, null=True,
                               related_name='group')

    def __str__(self):
        return f"{self.title} : {self.parent}"

    class Meta:
        verbose_name = "Группа наменклатуры"
        verbose_name_plural = 'Группы наменклатура'


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(verbose_name="Наименование", max_length=250)
    group = models.ForeignKey(ProductsGroup, on_delete=models.PROTECT, blank=True, null=True, related_name="prodocts", verbose_name="Группа")


    def __str__(self):
        return f'{self.full_name} - {self.group}'

    class Meta:
        verbose_name = "Наменклатуры"
        verbose_name_plural = 'Наменклатура'

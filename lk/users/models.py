import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    COMPANY = 'COMP'
    PRIVATE_PERSON = 'PRIV'
    COMPANY_PRIVATE = [
        (COMPANY, "Компания"),
        (PRIVATE_PERSON, 'Частное лицо')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=250, verbose_name='Наименование полное',
                                 unique=True, null=True, blank=True)
    status = models.CharField(verbose_name='Юр/Физ лицо', max_length=50, choices=COMPANY_PRIVATE, default=COMPANY)




# Create your models here.

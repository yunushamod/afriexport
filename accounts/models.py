from distutils.command.upload import upload
from email.policy import default
import imp
from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    class CompanyType(models.TextChoices):
        BUYER = "BY", "Buyer"
        SELLER = "SL", "Seller"
        FREIGHT_FORWARDER = "FF", "Freight Forwarder"
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=350)
    business_type = models.CharField(max_length=2, choices=CompanyType.choices, default=CompanyType.BUYER)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    country = models.CharField(max_length=200, default = 'Nigeria')
    state = models.CharField(max_length=200, default = 'Lagos')

    def __str__(self): return f'Profile of {self.user.username}'
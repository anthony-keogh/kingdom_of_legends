from django.db import models

# Create your models here.

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class purchase_product(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
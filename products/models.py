from django.db import models

# Create your models here.

# Create your models here.
from django.db import models

class Product_item(models.Model):
    name = models.CharField(max_length=200, default='', primary_key=True)
    description = models.TextField(max_length=600,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
   

    def __str__(self):
        return self.name
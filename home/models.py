from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import User
import re

class Select(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    item = models.CharField(max_length=60, null=True, blank=True,)
    quantity = models.CharField(max_length=12, null=True, blank=True,)
    price = models.CharField(max_length=20, null=True, blank=True)
    
    class Meta:
        db_table = "select"
        
    def total_price(self):
        return self.price * self.quantity

class Address(models.Model):
    address = models.CharField(max_length=60, null=True, blank=True,)
    state = models.CharField(max_length=60, null=True, blank=True,)
    country = models.CharField(max_length=60, null=True, blank=True,)
    postalcode = models.CharField(max_length=20, null=True, blank=True,)
    
    class Meta:
        db_table = "address"

    


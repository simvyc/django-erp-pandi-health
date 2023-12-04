from django.db import models
from django.urls import reverse

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True)
    material = models.CharField(max_length=20, blank=False)
    dimensions = models.CharField(max_length=35, blank=True)
    quantity = models.IntegerField(max_length=10, blank=True)
    leadtime = models.DateField()
    order_desing = models.ImageField(upload_to='photos/designs', blank=True)
    
    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        
    def __str__(self):
        return self.order_number
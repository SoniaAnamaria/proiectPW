from django.db import models


# Create your models here.
class Car(models.Model):
    color = models.CharField(max_length=50, default='green')
    tyre_type = models.CharField(max_length=10, blank=True, null=True)

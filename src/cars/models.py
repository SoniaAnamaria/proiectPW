from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

# Create your models here.
class Car(models.Model):
    color = models.CharField(max_length=50, default='green')
    tyre_type = models.CharField(max_length=10, blank=True, null=True)
    number_of_doors = models.IntegerField(verbose_name="Nr. doors", default=4)
    contact_email = models.EmailField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    last_revision = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

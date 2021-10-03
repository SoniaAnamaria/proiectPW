from django.contrib import admin

# Register your models here.
from cars.models import Car, Person

admin.site.register(Car)
admin.site.register(Person)
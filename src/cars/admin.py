from django.contrib import admin

# Register your models here.
from cars.models import Car, Person

class CarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Car)
admin.site.register(Person)
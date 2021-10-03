from django.contrib import admin

# Register your models here.
from cars.models import Car, Person

class CarAdmin(admin.ModelAdmin):
    list_display = ('__str__',  'tyre_type', 'contact_email', 'owner')
    list_editable = ('contact_email', 'owner')
    list_filter = ('owner',)
    search_fields = ('color', 'owner__last_name')
    fieldsets = [
        ['Informatii generale', {'fields': ('contact_email', 'owner')}],
        ['Detalii', {'fields': ('tyre_type', 'color')}]
    ]

class CarInline(admin.TabularInline):
    model = Car
    extra = 0
    fields = ('color', 'contact_email', 'tyre_type')

class PersonAdmin(admin.ModelAdmin):
    inlines = [CarInline]

admin.site.register(Car,CarAdmin)
admin.site.register(Person,PersonAdmin)
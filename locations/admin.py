from django.contrib import admin
from .models import Location

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'city',
        'address',
        'phone_number',
        'opening_hours',
    )

admin.site.register(Location, LocationAdmin)
from django.contrib import admin
from .models import Driver
from .models import Car


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

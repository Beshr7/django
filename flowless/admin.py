from django.contrib import admin
from .models import Pressure_Sensor, Pressure_Reading

# Register your models here.

admin.site.register(Pressure_Sensor)
admin.site.register(Pressure_Reading)

from django.contrib import admin
from sensorLoggingApi.models import EventData, SensorData
# Register your models here.

admin.site.register(EventData)
admin.site.register(SensorData)


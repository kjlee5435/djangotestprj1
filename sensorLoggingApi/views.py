from django.shortcuts import render
from sensorLoggingApi.models import EventData, SensorData
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

def index(request):
    print("index in")
    sensor_data_list = SensorData.objects.all().order_by('-pub_date')
    context = {'sensor_data_list': sensor_data_list}
    return render(request, 'sensorLoggingApi/index.html', context)
    
def submit(request):
    print("{0}, {1}, {2}".format(request.GET['key'],request.GET['humid'],request.GET['temperature']))

    if request.GET['key'] in "KgDWaHd3Vy8":
        d_humid = float(request.GET['humid'])
        d_temperature = float(request.GET['temperature'])
        newData = SensorData(humid=d_humid, temperature = d_temperature, pub_date=timezone.now())
        newData.save()
    else:
        print("key is not matching.")
    
    return HttpResponse(status=202)
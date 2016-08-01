from django.shortcuts import render
from sensorLoggingApi.models import EventData, SensorData
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import uuid

# Create your views here.

def index(request):
    print("index in")
    sensor_data_list = SensorData.objects.all().order_by('-pub_date')
    event_video_list = EventData.objects.all().order_by('-pub_date')

    context = {'sensor_data_list': sensor_data_list, 'event_video_list': event_video_list}
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
    
@csrf_exempt
def postfile(request):
    print("POSTFILE")
    if request.method == 'POST':
        print("POST")
        handle_uploaded_file(request.FILES['upload_file'])
        return HttpResponse(status=202)
    else:
        print("ERR1")
        return HttpResponse(status=1001)
        
def handle_uploaded_file(f):
    unique_filename = "{0}.mp4".format(uuid.uuid4())
    print("FILE PATH : {0}".format(os.path.join(settings.STATIC_ROOT, unique_filename)))
    
    newData = EventData(fileName=unique_filename, pub_date=timezone.now())
    newData.save()
    
    with open(os.path.join(settings.STATIC_ROOT, unique_filename), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
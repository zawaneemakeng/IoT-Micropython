from django.shortcuts import render
from django.http import HttpResponse
from .models import *

######## ---API LIBRARY--- ############
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TempHumidSerializer


def Home(request):  # กรณีไม่ทราบว่าจะไปหาใคร
    return HttpResponse('<h1><b>Hello World</b></h1>')


def Table(request):
    return HttpResponse('<h1>TEMP : 27 <br>HUMIDITY : 89 </h1>')


@api_view(['POST'])
def api_post_sensor(request):
    print(' POST DATA from ESP32 ')

    if request.method == 'POST':
        ser = TempHumidSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])  # user =ได้เฉพาะ post
# def api_post_sensortemphumid(request):

#     if request.method == 'POST':
#         try:
#             serializer = SensorTempHumidSerializer(data=request.data)
#             print('TYPE: ', type(request.data))
#             print('REQ DATA: ', request.data)

#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#         except:
#             print('R:', request.data)
#             data = json.loads(request.data)
#             print(data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

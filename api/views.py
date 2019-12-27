from django.shortcuts import render

from rest_framework import viewsets

from .serializer import TrainInfoSerializer
from .models import TrainInfo
from django.http import Http404

from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework.decorators import api_view

@api_view(['GET'])
def get_train_info(request):
    train_num = request.GET.get('train_num',None)
    if not train_num:
        raise Http404
    data=TrainInfo.objects.filter(train_num=train_num).first()
    if not data:
        raise Http404
    serial=TrainInfoSerializer(data)
    return Response(serial.data)


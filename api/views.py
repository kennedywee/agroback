from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


from api.models import Device, Data
from .serializers import DeviceSerializer, DataSerializer


class DataList(APIView):

    def get(self, request, format=None):
        api_key = request.GET['api_key']
        device = get_object_or_404(Device, api_key=api_key)
        datas = Data.objects.filter(device=device.id)

        serializer = DataSerializer(datas, many=True)
        return Response(serializer.data)

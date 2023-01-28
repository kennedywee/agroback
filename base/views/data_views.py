from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from base.models import Device, Data
from base.serializers import DataSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyData(request, pk):

    device = get_object_or_404(Device, id=pk)
    data = device.data_set.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)


class DataList(APIView):

    def get(self, request, format=None):
        api_key = request.GET['api_key']
        device = get_object_or_404(Device, api_key=api_key)
        datas = Data.objects.filter(device=device.id)

        serializer = DataSerializer(datas, many=True)
        return Response(serializer.data)


class CreateData(generics.ListCreateAPIView):

    serializer_class = DataSerializer

    def get(self, request, *args, **kwargs):
        api_key = request.GET['api_key']
        device = get_object_or_404(Device, api_key=api_key)

        latest_data = Data.objects.filter(
            device=device).order_by('-created').first()

        field1 = request.GET.get(
            'field1', latest_data.field1 if latest_data else None)
        field2 = request.GET.get(
            'field2', latest_data.field2 if latest_data else None)
        field3 = request.GET.get(
            'field3', latest_data.field3 if latest_data else None)
        field4 = request.GET.get(
            'field4', latest_data.field4 if latest_data else None)
        field5 = request.GET.get(
            'field5', latest_data.field5 if latest_data else None)

        new_data = Data.objects.create(device=device,
                                       field1=field1,
                                       field2=field2,
                                       field3=field3,
                                       field4=field4,
                                       field5=field5)
        new_data.save()

        serializer = DataSerializer(new_data)

        return Response(serializer.data)

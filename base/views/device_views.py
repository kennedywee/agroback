from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Device
from base.serializers import DeviceSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyDevices(request):
    user = request.user
    devices = user.device_set.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDevice(request, pk):
    device = Device.objects.get(id=pk)
    serializer = DeviceSerializer(device, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createDevice(request):
    user = request.user
    data = request.data
    print(data)

    device = Device.objects.create(
        user=user,
        name=data['name'],
        device_type=data['device_type'],
        location=data['location'],
        field1=data['field1'],
        field2=data['field2'],
        field3=data['field3'],
        field4=data['field4'],
        field5=data['field5'],
        type_field1=data['type_field1'],
        type_field2=data['type_field2'],
        type_field3=data['type_field3'],
        type_field4=data['type_field4'],
        type_field5=data['type_field5'],
        description=data['description'],
    )

    device.save()
    serializer = DeviceSerializer(device, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteDevice(request, pk):
    device = Device.objects.get(id=pk)
    device.delete()
    return Response("Device is successfully deleted!")


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateDevice(request, pk):
    data = request.data
    device = Device.objects.get(id=pk)

    for key, value in data.items():
        setattr(device, key, value)

    device.save()
    serializer = DeviceSerializer(device, many=False)
    return Response(serializer.data)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from base.models import Schedule, Device
from base.serializers import ScheduleSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMySchedules(request):
    user = request.user
    schedules = user.schedule_set.all()
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSchedule(request, pk):
    schedule = Schedule.objects.get(id=pk)
    serializer = ScheduleSerializer(schedule, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createSchedule(request):
    user = request.user
    data = request.data

    id = request.data["device"]
    device = get_object_or_404(Device, id=id)

    schedule = Schedule.objects.create(
        user=user,
        device=device,
        name=data['name'],
        datetime=data['datetime'],
        duration=data['duration'],
        field=data['field'],
    )

    schedule.save()
    serializer = ScheduleSerializer(schedule, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateSchedule(request, pk):
    data = request.data
    schedule = Schedule.objects.get(id=pk)

    for key, value in data.items():
        if key == "device":
            value = Device.objects.get(id=value)
        setattr(schedule, key, value)

    schedule.save()
    serializer = ScheduleSerializer(schedule, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteSchedule(request, pk):
    schedule = Schedule.objects.get(id=pk)
    schedule.delete()
    return Response("Schedule is successfully deleted!")

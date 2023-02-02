from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from base.models import Alert, Device
from base.serializers import AlertSerializer


from django.core.mail import send_mail
from django.conf import settings


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyAlerts(request):
    user = request.user
    alerts = user.alert_set.all()
    serializer = AlertSerializer(alerts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAlert(request, pk):
    alert = Alert.objects.get(id=pk)
    serializer = AlertSerializer(alert, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAlert(request):
    user = request.user
    data = request.data

    id = request.data["device"]

    device = get_object_or_404(Device, id=id)

    alert = Alert.objects.create(
        user=user,
        device=device,
        name=data['name'],
        field=data['field'],
        condition_value=data['condition_value'],
        message=data['message'],
        frequency=data['frequency'],
    )

    alert.save()
    serializer = AlertSerializer(alert, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateAlert(request, pk):
    data = request.data
    alert = Alert.objects.get(id=pk)

    for key, value in data.items():
        if key == "device":
            value = Device.objects.get(id=value)
        setattr(alert, key, value)

    alert.save()
    serializer = AlertSerializer(alert, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteAlert(request, pk):
    alert = Alert.objects.get(id=pk)
    alert.delete()
    return Response("Alert is successfully deleted!")


def send_alert_email(alert):
    subject = 'Alert triggered: {}'.format(alert.name)
    message = 'The alert {} has been triggered for device {}. The message is: {}'.format(
        alert.name,
        alert.device,
        alert.message
    )
    recipient_list = [alert.user.email]
    send_mail(subject, message, 'from@example.com', recipient_list)


def send_alert_email_test(request):

    alert = Alert.objects.get(id=8)
    email_host = settings.EMAIL_HOST_USER

    subject = 'Alert triggered: {}'.format(alert.name)
    message = 'The alert {} has been triggered for device {}. The message is: {}'.format(
        alert.name,
        alert.device,
        alert.message
    )
    recipient_list = [alert.user.email]
    send_mail(subject, message, email_host, recipient_list)

    return Response("email sent")

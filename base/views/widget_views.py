from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from rest_framework import generics
from rest_framework import serializers


from base.models import Widget
from base.serializers import WidgetSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyWidgets(request):
    user = request.user
    widgets = user.widget_set.all()
    serializer = WidgetSerializer(widgets, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateWidget(request, pk):
    data = request.data
    widget = Widget.objects.get(i=pk)

    for key, value in data.items():
        setattr(widget, key, value)

    widget.save()
    serializer = WidgetSerializer(widget, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createWidget(request):
    user = request.user

    widget = Widget.objects.create(user=user)

    widget.save()
    serializer = WidgetSerializer(widget, many=False)
    return Response(serializer.data)

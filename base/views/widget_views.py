from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Widget
from base.serializers import WidgetSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyWidgets(request):
    user = request.user
    widgets = user.widget_set.all()
    serializer = WidgetSerializer(widgets, many=True)
    return Response(serializer.data)

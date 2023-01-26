from rest_framework import serializers
from api.models import Device, Data


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = "__all__"


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = "__all__"

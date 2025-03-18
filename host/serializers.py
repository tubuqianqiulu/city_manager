from rest_framework import serializers
from .models import City, MachineRoom, Host


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class MachineRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineRoom
        fields = '__all__'


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

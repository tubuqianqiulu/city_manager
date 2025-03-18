import subprocess
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import City, MachineRoom, Host
from .serializers import CitySerializer, MachineRoomSerializer, HostSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class MachineRoomViewSet(viewsets.ModelViewSet):
    queryset = MachineRoom.objects.all()
    serializer_class = MachineRoomSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


def ping_host(request, ip_address):
    try:
        result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return Response({'status': 'reachable'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'unreachable'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

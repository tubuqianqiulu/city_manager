import subprocess
from django.http import JsonResponse
from django.views import View
from .models import Host, City, MachineRoom, HostCountStatistics
from django.utils import timezone
from django.db.models import Count


class HostListCreateView(View):
    def get(self, request):
        hosts = Host.objects.all()
        data = [{'id': host.id, 'ip': host.ip, 'machine_room': host.machine_room.id} for host in hosts]
        return JsonResponse(data, safe=False)

    def post(self, request):
        ip = request.POST.get('ip')
        machine_room_id = request.POST.get('machine_room')
        try:
            machine_room = MachineRoom.objects.get(id=machine_room_id)
            host = Host.objects.create(ip=ip, machine_room=machine_room)
            return JsonResponse({'id': host.id, 'ip': host.ip, 'machine_room': host.machine_room.id})
        except MachineRoom.DoesNotExist:
            return JsonResponse({'error': 'Machine room not found'}, status=404)


class HostRetrieveUpdateDestroyView(View):
    def get(self, request, pk):
        try:
            host = Host.objects.get(id=pk)
            return JsonResponse({'id': host.id, 'ip': host.ip, 'machine_room': host.machine_room.id})
        except Host.DoesNotExist:
            return JsonResponse({'error': 'Host not found'}, status=404)

    def put(self, request, pk):
        try:
            host = Host.objects.get(id=pk)
            ip = request.POST.get('ip', host.ip)
            machine_room_id = request.POST.get('machine_room', host.machine_room.id)
            try:
                machine_room = MachineRoom.objects.get(id=machine_room_id)
                host.ip = ip
                host.machine_room = machine_room
                host.save()
                return JsonResponse({'id': host.id, 'ip': host.ip, 'machine_room': host.machine_room.id})
            except MachineRoom.DoesNotExist:
                return JsonResponse({'error': 'Machine room not found'}, status=404)
        except Host.DoesNotExist:
            return JsonResponse({'error': 'Host not found'}, status=404)

    def delete(self, request, pk):
        try:
            host = Host.objects.get(id=pk)
            host.delete()
            return JsonResponse({'message': 'Host deleted successfully'})
        except Host.DoesNotExist:
            return JsonResponse({'error': 'Host not found'}, status=404)


class PingHostView(View):
    def get(self, request, pk):
        try:
            host = Host.objects.get(id=pk)
            try:
                result = subprocess.run(['ping', '-c', '1', host.ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                is_reachable = result.returncode == 0
                return JsonResponse({'is_reachable': is_reachable})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        except Host.DoesNotExist:
            return JsonResponse({'error': 'Host not found'}, status=404)


def daily_statistics():
    now = timezone.now().date()
    statistics = Host.objects.values('machine_room__city', 'machine_room').annotate(count=Count('id'))
    for stat in statistics:
        city = City.objects.get(id=stat['machine_room__city'])
        machine_room = MachineRoom.objects.get(id=stat['machine_room'])
        HostCountStatistics.objects.create(city=city, machine_room=machine_room, count=stat['count'], date=now)    
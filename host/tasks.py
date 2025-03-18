from celery import shared_task
from .models import City, MachineRoom, Host


@shared_task
def daily_host_count_statistics():
    cities = City.objects.all()
    for city in cities:
        machine_rooms = MachineRoom.objects.filter(city=city)
        for machine_room in machine_rooms:
            host_count = Host.objects.filter(machine_room=machine_room).count()

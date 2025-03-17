from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MachineRoom(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Host(models.Model):
    ip = models.GenericIPAddressField()
    machine_room = models.ForeignKey(MachineRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip


class HostCountStatistics(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    machine_room = models.ForeignKey(MachineRoom, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.city.name} - {self.machine_room.name} - {self.count} - {self.date}' 
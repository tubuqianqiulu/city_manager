from django.db import models


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
    ip_address = models.GenericIPAddressField()
    machine_room = models.ForeignKey(MachineRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip_address

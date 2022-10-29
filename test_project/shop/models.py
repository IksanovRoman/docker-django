from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)
    house = models.IntegerField()
    time_open = models.TimeField()
    time_close = models.TimeField()
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    street = models.ForeignKey('Street', on_delete=models.PROTECT)

    def __str__(self):
        return f"Город: {self.city}, улица: {self.street}, магазин: {self.name}"

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

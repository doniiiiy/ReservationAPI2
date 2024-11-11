from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    addres = models.CharField(max_length=255)
    descruption = models.TextField()


    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='tables', on_delete=models.CASCADE)
    number = models.IntegerField()
    capacity = models.IntegerField()


    def __str__(self):
        return f'Table {self.number} at {self.restaurant.name}'



class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()

def __str__(self):
    return f'{self.user.username} reserved {self.table} at {self.reservation_time}'
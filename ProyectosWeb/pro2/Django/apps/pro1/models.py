from django.db import models

# Create your models here.

class Payment(models.Model):
    method_pay = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.id} - {self.method_pay}'

class Extras(models.Model):
    addres = models.CharField(max_length=100)
    altitude = models.IntegerField() 
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_update = models.IntegerField()
    normal_bikes = models.IntegerField()
    payment = models.ManyToManyField(Payment)
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=10, null=True, blank=True)
    renting = models.IntegerField()
    returning = models.IntegerField()
    slot = models.IntegerField()
    uid = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.id} {self.addres}'


class Station(models.Model):
    number_station = models.IntegerField()
    empty_slots = models.IntegerField()
    extras = models.ForeignKey(Extras, on_delete=models.CASCADE)
    free_bikes = models.IntegerField()
    id_token = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'


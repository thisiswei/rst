from django.db import models
from django.contrib.auth.models import User
from rstutils import HasState
from rstdjango import Position

POSITION = [(p, p) for p in Position]

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=16)
    creditcard_number = models.CharField(max_length=16)

class Restaurant(HasState):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    lat = models.FloatField(max_length=16)
    lon = models.FloatField(max_length=16)
    addr = models.TextField(max_length=124)

class Job(HasState):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
    position = models.CharField(
            max_length=16,
            choice=POSITION,
            default=POSITION[0][0],
            )
    salary = models.FloatField()
    description = models.TextField(max_length=256)

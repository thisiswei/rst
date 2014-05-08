from django.db import models
from django.contrib.auth.models import User
from rstdjango import Position

POSITION = [(p, p) for p in Position]

STATE_CHOICES = [(t, t) for t in ('active', 'inactive')]

class HasState(models.Model):
    state = models.CharField(
            max_length=16,
            choices=STATE_CHOICES,
            default=STATE_CHOICES[0][0],
            )

    @classmethod
    def filter(cls, **kwargs):
        kwargs['state'] = 'active'
        return cls.objects.filter(kwargs)

    class Meta:
        abstract = True

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=16)
    creditcard_number = models.CharField(max_length=16)

    def __unicode__(self):
        return self.user.username

class Restaurant(HasState):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    lat = models.FloatField(max_length=16)
    lon = models.FloatField(max_length=16)
    zip_code = models.CharField(max_length=8)
    addr = models.TextField(max_length=124)

    def __unicode__(self):
        return self.name

class Job(HasState):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
    position = models.CharField(
            max_length=16,
            choices=POSITION,
            default=POSITION[0][0],
            )
    salary = models.FloatField()
    description = models.TextField(max_length=256)

    def __unicode__(self):
        return self.position

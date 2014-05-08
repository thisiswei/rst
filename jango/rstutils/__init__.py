from django.db import models

STATE_CHOICES = [(t, t) for t in ('active', 'inactive')]

class HasState(models.Model):
    state = models.CharField(
            max_length=16,
            choices=STATE_CHOICES,
            #default=STATE_CHOICES[0][0],
            )

    @classmethod
    def filter(cls, **kwargs):
        kwargs['state'] = 'active'
        return cls.objects.filter(kwargs)

    class Meta:
        abstract = True

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from rstdjango.models import Job, Restaurant
from django.contrib.auth.models import User

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff']
        allowed_methods = ['get']

class RestaurantResource(ModelResource):
    class Meta:
        queryset = Restaurant.objects.all()
        resource_name = 'restaurant'


class JobResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    restaurant = fields.ForeignKey(RestaurantResource, 'restaurant')

    class Meta:
        queryset = Job.objects.all()
        authorization = Authorization()
        resource_name = 'job'


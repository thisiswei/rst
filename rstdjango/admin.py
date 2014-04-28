from django.contrib import admin
from rstdjango.models import Job, Restaurant

class JobAdmin(admin.ModelAdmin):
    pass
admin.site.register(Job, JobAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Restaurant, RestaurantAdmin)

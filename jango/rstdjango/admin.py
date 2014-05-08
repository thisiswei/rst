from django.contrib import admin
from rstdjango.models import Job, Restaurant, UserProfile

class JobAdmin(admin.ModelAdmin):
    pass
admin.site.register(Job, JobAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Restaurant, RestaurantAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)

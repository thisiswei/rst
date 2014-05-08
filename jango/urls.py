from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from rstdjango.api import JobResource, UserResource, RestaurantResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(JobResource())
v1_api.register(RestaurantResource())

admin.autodiscover()
job_resource = JobResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jango.views.home', name='home'),
    # url(r'^jango/', include('jango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)

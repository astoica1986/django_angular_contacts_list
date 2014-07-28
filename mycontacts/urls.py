from django.conf.urls import patterns, include, url
from contacts.api import ContactResource
from django.contrib import admin
from contacts import views


admin.autodiscover()

contact_resource_api = ContactResource()
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^export/$', views.export),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(contact_resource_api.urls)),

)


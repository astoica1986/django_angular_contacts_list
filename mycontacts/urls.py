from django.conf.urls import patterns, include, url
from contacts.api import ContactResource
from django.contrib import admin
from contacts import views
from django.views.generic.base import TemplateView

admin.autodiscover()

contact_resource_api = ContactResource()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mycontacts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(contact_resource_api.urls)),

)


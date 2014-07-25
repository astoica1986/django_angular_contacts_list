
# api.py
"""
Example REST API
"""
from tastypie.validation import FormValidation
from contacts.models import Contact
from contacts.forms import ContactForm
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization


class ContactResource(ModelResource):
    class Meta:
        resource_name = 'contacts'
        allowed_methods = ['get', 'post', 'put', 'delete']
        queryset = Contact.objects.all()
        authorization = Authorization()
        validation = FormValidation(form_class=ContactForm)
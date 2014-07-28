from import_export import resources
from contacts.models import Contact


class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
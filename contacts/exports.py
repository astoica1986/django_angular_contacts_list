from import_export import resources
from contacts.models import Contact


class ContactsResource(resources.ModelResource):
    class Meta:
        model = Contact
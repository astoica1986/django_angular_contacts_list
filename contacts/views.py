from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from contacts.exports import ContactResource
from contacts.models import Contact
from contacts.forms import UploadFileForm
import tablib


def index(request, template_name='index.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))


def export(request):
    allowed_export_formats = ['json', 'csv', 'xml']
    format_type = request.GET.get('format_type')
    if format_type in allowed_export_formats:
        dataset = export_xml() if format_type == 'xml' else ContactResource().export()
        response = HttpResponse(mimetype="text/{}".format(format_type))
        response['Content-Disposition'] = "attachment; filename=contact_list.{}".format(format_type)
        response.write(dataset if format_type == 'xml' else getattr(dataset, format_type))
        return response
    else:
        return HttpResponseBadRequest()


def export_xml():
    return serializers.serialize("xml", Contact.objects.all())


def import_data(request):
    # dataset = tablib.Dataset()
    #dataset.headers = ['id', 'firstName', 'lastName', 'phone', 'email']
    pass
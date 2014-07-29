import csv
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from import_export import resources
from contacts.models import Contact
from contacts.forms import UploadFileForm
import json
import tablib
import xmldict
import dicttoxml

def index(request, template_name='index.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))


def export(request):

    format_type = request.GET.get('format_type')
    if format_type in allowed_export_formats():
        #contact_resource = resources.modelresource_factory(model=Contact)()
        cons = [obj.as_dict() for obj in Contact.objects.all()]
        response = HttpResponse(mimetype="text/{}".format(format_type))
        response['Content-Disposition'] = "attachment; filename=contact_list.{}".format(format_type)
        if format_type == 'json':
            ser = json.dumps(cons)
            response.write(ser)
        elif format_type == 'xml':
            ser = dicttoxml.dicttoxml(cons)
            response.write(ser)
        else:
            response = export_csv(response, cons)

        return response
    else:
        return HttpResponseBadRequest()


def export_csv(response, cons):
    writer = csv.writer(response)
    writer.writerow(['firstName', 'lastName', 'phone', 'email'])
    for c in cons:
        writer.writerow([c['firstName'], c['lastName'], c['phone'], c['email']])
    return response


def import_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        imported_file = request.FILES['uploadField'].read()
        format_type = str(request.FILES['uploadField']).split(".")[-1].lower()
        if form.is_valid() and format_type in allowed_export_formats():
            if format_type == 'json':
                for json_contact in json.loads(imported_file):
                    contact = Contact(firstName=json_contact['firstName'], lastName=json_contact['lastName'],
                                      phone=json_contact['phone'], email=json_contact['email'])
                    contact.save()
            elif format_type == 'xml':
                print xmldict.xml_to_dict(imported_file)
        else:
            print(form.errors)
        return render_to_response('index.html', context_instance=RequestContext(request))


def import_xml(file):
    pass


def import_standard_mime(file, format_type):
    dataset = tablib.Dataset()
    contact_resource = resources.modelresource_factory(model=Contact)()
    dataset.headers = ['firstName', 'lastName', 'email', 'phone']
    #setattr(dataset, format_type, file)
    dataset.csv = file

    result = contact_resource.import_data(dataset, dry_run=True, raise_errors=True)
    print(result)


def allowed_export_formats():
    return ['json', 'csv', 'xml']
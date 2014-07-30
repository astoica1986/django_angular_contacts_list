from django.forms import model_to_dict
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest
from contacts.models import Contact
from contacts.forms import UploadFileForm
import json
import xmldict
import dicttoxml
import csv


def index(request, template_name='index.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))


def export(request):
    format_type = request.GET.get('format_type')
    if format_type in allowed_export_formats():
        # contact_resource = resources.modelresource_factory(model=Contact)()
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
                import_json(imported_file)
            elif format_type == 'xml':
                import_xml(imported_file)
            else:
                import_csv(imported_file)
        else:
            print(form.errors)
        return render_to_response('index.html', context_instance=RequestContext(request))


def import_xml(imported_file):
    raw_xml = xmldict.xml_to_dict(imported_file)['root']['item']
    for item in raw_xml:
        contact = Contact(firstName=item['firstName']['#text'], lastName=item['lastName']['#text'],
                          phone=item['phone']['#text'], email=item['email']['#text'])
        contact.save()


def import_json(imported_file):
    for json_contact in json.loads(imported_file):
        contact = Contact(firstName=json_contact['firstName'], lastName=json_contact['lastName'],
                          phone=json_contact['phone'], email=json_contact['email'])
        contact.save()


def import_csv(imported_file):
    for i, v in enumerate(imported_file.splitlines()):
        if i == 0:
            continue
        else:
            v = v.split(',')
            contact = Contact(firstName=v[0], lastName=v[1], phone=v[2], email=v[3])
            contact.save()


def allowed_export_formats():
    return ['json', 'csv', 'xml']
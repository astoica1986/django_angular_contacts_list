from django import forms
from contacts.models import Contact
import re


class ContactForm(forms.ModelForm):
    phone = forms.RegexField('0([0-9]{9})', max_length=12, min_length=10, error_message='Enter a valid romanian telephone number')

    class Meta:
        model = Contact


class UploadFileForm(forms.Form):
    uploadField  = forms.FileField()
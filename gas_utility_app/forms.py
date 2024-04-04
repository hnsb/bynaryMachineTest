from django import forms
from .models import ServiceRequest, FileAttachment

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details']

class FileAttachmentForm(forms.ModelForm):
    class Meta:
        model = FileAttachment
        fields = ['file']

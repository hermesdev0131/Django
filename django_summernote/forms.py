from django import forms

from django_summernote.utils import get_attachment_model


class UploadForm(forms.Form):
    file = forms.ImageField(required=True)


class AttachmentAdminForm(forms.ModelForm):
    file = forms.ImageField(required=True)

    class Meta:
        model = get_attachment_model()
        fields = '__all__'

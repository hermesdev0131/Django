from django.urls import path

from django_summernote.views import (
    SummernoteEditor, SummernoteUploadAttachment
)

urlpatterns = [
    path('editor/<id>/', SummernoteEditor.as_view(),
        name='django_summernote-editor'),
    path('upload_attachment/', SummernoteUploadAttachment.as_view(),
        name='django_summernote-upload_attachment'),
]

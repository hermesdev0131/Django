from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.db import models

from django_summernote.forms import AttachmentAdminForm
from django_summernote.utils import get_attachment_model, get_config
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SummernoteModelAdminMixin:
    summernote_fields = '__all__'

    def formfield_for_dbfield(self, db_field, *args, **kwargs):
        summernote_widget = SummernoteWidget if get_config()['iframe'] else SummernoteInplaceWidget

        if self.summernote_fields == '__all__':
            if isinstance(db_field, models.TextField):
                kwargs['widget'] = summernote_widget
        else:
            if db_field.name in self.summernote_fields:
                kwargs['widget'] = summernote_widget

        return super().formfield_for_dbfield(db_field, *args, **kwargs)


class SummernoteInlineModelAdmin(SummernoteModelAdminMixin, InlineModelAdmin):
    pass


class SummernoteModelAdmin(SummernoteModelAdminMixin, admin.ModelAdmin):
    pass


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'uploaded']
    search_fields = ['name']
    ordering = ('-id',)
    form = AttachmentAdminForm


if not get_config()['disable_attachment']:
    admin.site.register(get_attachment_model(), AttachmentAdmin)

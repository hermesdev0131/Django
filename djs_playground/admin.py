# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from .models import Post, Book, Author


class PostAdmin(SummernoteModelAdmin):
    pass


class BookInline(SummernoteModelAdminMixin, admin.StackedInline):
    model = Book


class AuthorAdmin(SummernoteModelAdminMixin, admin.ModelAdmin):
    model = Author
    inlines = [
        BookInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)

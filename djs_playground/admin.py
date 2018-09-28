# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from .models import Post, Book, Author

class BookAdmin(admin.ModelAdmin):
    model = Book
    pass


class PostAdmin(SummernoteModelAdmin):
    pass


class BookInline(SummernoteModelAdminMixin, admin.StackedInline):
    model = Book
    extra = 1


class AuthorAdmin(SummernoteModelAdminMixin, admin.ModelAdmin):
    model = Author
    inlines = [
        BookInline,
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)

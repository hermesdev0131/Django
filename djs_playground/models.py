# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Sample model for testing admin page
class Post(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")
    body = models.TextField(blank=True, null=True)

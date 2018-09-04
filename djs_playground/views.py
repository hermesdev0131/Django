# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .settings import SUMMERNOTE_THEME


class SampleForm(forms.Form):
    desc1 = forms.CharField(
        label='iframe',
        widget=SummernoteWidget()
    )
    desc2 = forms.CharField(
        label='in place',
        widget=SummernoteInplaceWidget()
    )
    desc3 = forms.CharField(
        label='normal field',
        widget=forms.Textarea
    )


def index(request):
    return render(request, 'index.html', {
        'desc1': request.POST.get('desc1'),
        'desc2': request.POST.get('desc2'),
        'form': SampleForm(),
        'theme': SUMMERNOTE_THEME,
    })

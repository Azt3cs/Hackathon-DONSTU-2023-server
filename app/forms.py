from django import forms
from .models import *

class addPari(forms.Form):
    predmet = forms.CharField(max_length=20, blank=False)
    prepod = forms.CharField(max_length=20, blank=False)
    group = forms.CharField(max_length=20, blank=False)
    date = models.DateTimeField()
    auditoria = models.IntegerField()


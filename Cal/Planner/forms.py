from django import forms
from django.db import models
from .models import Item, User

from django.contrib.admin import widgets

class DateInput(forms.DateInput):
    input_type = 'date'

class NewItemForm(forms.ModelForm):
    early_start_time=forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_attrs={"placeholder":"yyyy-mm-dd"}, time_attrs={"placeholder":"hh:mm:ss"}))
    late_start_time=forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_attrs={"placeholder":"yyyy-mm-dd"}, time_attrs={"placeholder":"hh:mm:ss"}))
    name=forms.CharField(widget=forms.TextInput(attrs={"autofocus":True}))
    class Meta:
        model=Item
        fields=["name", "early_start_time", "late_start_time", "duration", "priority"]

class UploadCalendarForm(forms.Form):
    cal=forms.FileField()
from django import forms
from django.db import models
from .models import Item

class DateInput(forms.DateInput):
    input_type = 'date'

class NewItemForm(forms.ModelForm):
    early_start_time=models.DateTimeField(forms.SplitDateTimeWidget(date_attrs={"placeholder":"yyyy-mm-dd"},time_attrs={"placeholder":"hh:mm:ss"}))
    late_start_time=models.DateTimeField(forms.SplitDateTimeWidget(date_attrs={"placeholder":"yyyy-mm-dd"},time_attrs={"placeholder":"hh:mm:ss"}))
    class Meta:
        model=Item
        fields=["name", "early_start_time", "late_start_time", "duration", "priority"]
        #widgets={
            #"early_start_time":forms.SplitDateTimeWidget(date_attrs={"placeholder":"yyyy-mm-dd"},time_attrs={"placeholder":"hh:mm:ss"}),
            #"late_start_time":forms.SplitDateTimeWidget(date_attrs={"placeholder":"yyyy-mm-dd"},time_attrs={"placeholder":"hh:mm:ss"})
        #}

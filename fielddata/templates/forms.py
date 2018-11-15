from django import forms
from django.forms import ModelForm
from .models import Dataset, Block, LocationBlock, TextBlock, MeasurementBlock


class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = ('name', 'template')
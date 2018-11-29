from django import forms
from django.forms import ModelForm
from .models import Dataset, Block, LocationBlock, TextBlock, MeasurementBlock, Template


class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = ('name', 'template',)

class TemplateForm(ModelForm):
    class Meta:
        model = Template
        fields = ('name',)

class BlockForm(ModelForm):
    class Meta:
        model = Block
        #fields = ('name',)
        exclude = ('template',)

class LocationBlockForm(ModelForm):
    class Meta:
        model = LocationBlock
        fields = ('westLong','eastLong','southLat','northLat',)

class TextBlockForm(ModelForm):
    class Meta:
        model = TextBlock
        fields = ('text',)

class MeasurementBlockForm(ModelForm):
    class Meta:
        model = MeasurementBlock
        fields = ('unit', 'measurement',)
from django import forms
from django.forms import modelformset_factory
from .models import Block, LocationBlock, TextBlock, MeasurementBlock

class BlockModelForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'


LocationBlockFormset = modelformset_factory(
    LocationBlock,
    fields = '__all__',
    extra=1
)
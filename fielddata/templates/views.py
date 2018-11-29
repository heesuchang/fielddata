# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from polymorphic.formsets import polymorphic_modelformset_factory, PolymorphicFormSetChild

from .forms import DatasetForm, TemplateForm, BlockForm, LocationBlockForm, MeasurementBlockForm, TextBlockForm
from .models import Dataset, Template, Block, LocationBlock, MeasurementBlock, TextBlock



def create_dataset(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST)
        if form.is_valid():
            template_id = form.cleaned_data.get('template')
            copy = Template.objects.get(pk=template_id)
            copy.pk = None
            copy.save()
            new_dataset = Dataset(name=form.cleaned_data.get('name'))
            new_dataset.save()
            new_dataset.template.add(Template.objects.get(pk=copy.pk))
            new_dataset.save()
            return redirect('dataset_list')
    else:
        form = DatasetForm()
    return render(request, 'create_dataset.html', {'form':form})

def edit_dataset(request, id=None, template_name='edit_dataset.html'):
    BlockFormSet = polymorphic_modelformset_factory(Block, formset_children=(
        PolymorphicFormSetChild(LocationBlock),
        PolymorphicFormSetChild(MeasurementBlock),
        PolymorphicFormSetChild(TextBlock),
    ), form=BlockForm)
    if request.method == 'POST':
        if id:
            dataset = Dataset.objects.get(pk=id)
            datasetName = dataset.name

        else:
            redirect('dataset_list')

        #form = DatasetForm(request.POST or None, instance=dataset)
        formset = BlockFormSet(request.POST or None, queryset=dataset.template.all().block.all())

        if formset.is_valid():
            formset.save()
            return redirect('dataset_list')
    else:
        formset = BlockFormSet()
        datasetName = 'None'

        if id:
            dataset = Dataset.objects.get(pk=id)
            datasetName = dataset.name
            template = Template.objects.filter(dataset__pk=id)[0]
            formset = BlockFormSet()

    return render(request, template_name, {'datasetName':datasetName, 'formset':formset})

class DatasetListView(ListView):
    model = Dataset
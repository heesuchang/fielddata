# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from .forms import DatasetForm
from .models import Dataset, Template


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
    if request.method == 'POST':
        if id:
            dataset = Dataset(Dataset, pk=id)
        else:
            redirect('dataset_list')

        form = DatasetForm(request.POST or None, instance=dataset)

        if form.is_valid():
            form.save()
            return redirect('dataset_list')
    else:
        form = DatasetForm()
    return render(request, template_name, {'form':form})

class DatasetListView(ListView):
    model = Dataset
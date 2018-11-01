# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import LocationBlockFormset, BlockModelForm
from .models import LocationBlock, TextBlock, MeasurementBlock


def index(request):
    return HttpResponse("Templates index.")

def create_template(request):
    template_name = 'create_template.html'
    if request.method == 'GET':
        blockform = BlockModelForm(request.GET or None)
        formset = LocationBlockFormset(queryset=LocationBlock.objects.none())
    elif request.method == 'POST':
        blockform = BlockModelForm(request.POST)
        formset = LocationBlockFormset(request.POST)
        if blockform.is_valid() and formset.is_valid():
            block = blockform.save()
            for form in formset:
                locationBlock = form.save(commit=False)
                locationBlock.block = block
                locationBlock.save()
            return redirect('template:block_list')
    return render(request, template_name, {
        'blockform': blockform,
        'formset': formset,
    })
# Create your views here.

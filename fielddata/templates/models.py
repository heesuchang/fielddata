# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from polymorphic.models import PolymorphicModel
from django.urls import reverse

class Template(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dataset(models.Model):
    template = models.ManyToManyField(Template)
    name = models.CharField(max_length=100)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dataset-detail', kwargs={'pk': self.pk})

class Block(PolymorphicModel):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class LocationBlock(Block):
    westLong = models.DecimalField(default=-180, max_digits=6, decimal_places=3)
    eastLong = models.DecimalField(default=180, max_digits=6, decimal_places=3)
    northLat = models.DecimalField(default=90, max_digits=6, decimal_places=3)
    southLat = models.DecimalField(default=-90, max_digits=6, decimal_places=3)

class TextBlock(Block):
    text = models.TextField(blank=True)

class MeasurementBlock(Block):
    unit = models.CharField(max_length=50, blank=True)
    measurement = models.IntegerField(default=0, blank=True)


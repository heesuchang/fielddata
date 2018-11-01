# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from polymorphic.admin import StackedPolymorphicInline, PolymorphicInlineSupportMixin
from .models import Template, Block, LocationBlock, TextBlock, MeasurementBlock

class BlockInLine(StackedPolymorphicInline):
    class TextBlockInline(StackedPolymorphicInline.Child):
        model = TextBlock
    class LocationBlockInline(StackedPolymorphicInline.Child):
        model = LocationBlock
    class MeasurementBlockInline(StackedPolymorphicInline.Child):
        model = MeasurementBlock

    model = Block

    child_inlines = (
        TextBlockInline,
        LocationBlockInline,
        MeasurementBlockInline,
    )

@admin.register(Template)
class TemplateAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = (BlockInLine,)

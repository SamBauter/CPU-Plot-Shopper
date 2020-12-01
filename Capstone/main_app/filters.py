import django_filters
from django import forms
from django_filters import MultipleChoiceFilter, RangeFilter
from .models import MonitorSpecs, CPUSpecs


def get_choices(model, field):
    choices = []
    for k in model.objects.values_list(field).order_by(field).distinct():
        choices.append((k[0], k[0]))
    return choices


class MonitorFilter(django_filters.FilterSet):
    brand = MultipleChoiceFilter(choices=get_choices(MonitorSpecs, 'brand'), widget=forms.CheckboxSelectMultiple)
    size = MultipleChoiceFilter(choices=get_choices(MonitorSpecs, 'size'), widget=forms.CheckboxSelectMultiple)
    resolution = MultipleChoiceFilter(choices=get_choices(MonitorSpecs, 'resolution'),
                                      widget=forms.CheckboxSelectMultiple)
    ref_rate = MultipleChoiceFilter(choices=get_choices(MonitorSpecs, 'ref_rate'), widget=forms.CheckboxSelectMultiple)
    res_rate = MultipleChoiceFilter(choices=get_choices(MonitorSpecs, 'res_rate'), widget=forms.CheckboxSelectMultiple)
    panel_type = MultipleChoiceFilter(choices=get_choices(MonitorSpecs, 'panel_type'),
                                      widget=forms.CheckboxSelectMultiple)
    asp_ratio = MultipleChoiceFilter(choices=get_choices(MonitorSpecs, 'asp_ratio'),
                                     widget=forms.CheckboxSelectMultiple)
    curved = MultipleChoiceFilter(choices=get_choices(MonitorSpecs, 'curved'), widget=forms.CheckboxSelectMultiple)

    # fix sync options to be a single field with a second field for gsync compat in db

    class Meta:
        model = MonitorSpecs
        fields = ['brand', 'size']


class CPUFilter(django_filters.FilterSet):
    brand = MultipleChoiceFilter(choices=get_choices(CPUSpecs, 'brand'), widget=forms.CheckboxSelectMultiple)
    model = MultipleChoiceFilter(choices=get_choices(CPUSpecs, 'model'), widget=forms.CheckboxSelectMultiple)
    core_count = MultipleChoiceFilter(choices=get_choices(CPUSpecs, 'core_count'),
                                      widget=forms.CheckboxSelectMultiple)
    boost_clock = MultipleChoiceFilter(choices=get_choices(CPUSpecs, 'boost_clock'),
                                       widget=forms.CheckboxSelectMultiple)
    tdp = MultipleChoiceFilter(choices=get_choices(CPUSpecs, 'tdp'), widget=forms.CheckboxSelectMultiple)
    integrated_graphics = MultipleChoiceFilter(choices=get_choices(CPUSpecs, 'integrated_graphics'),
                                               widget=forms.CheckboxSelectMultiple)
    smt = MultipleChoiceFilter(choices=get_choices(CPUSpecs, 'smt'),
                               widget=forms.CheckboxSelectMultiple)
    core_clock = MultipleChoiceFilter(choices=get_choices(CPUSpecs, 'core_clock'), widget=forms.CheckboxSelectMultiple)


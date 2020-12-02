import django_filters
from django import forms
from django_filters import MultipleChoiceFilter, RangeFilter
from .models import MonitorSpecs, CPUSpecs, GPUSpecs, MBSpecs, PSUSpecs, RAMSpecs, StorSpecs


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


class GPUFilter(django_filters.FilterSet):
    brand = MultipleChoiceFilter(choices=get_choices(GPUSpecs, 'brand'), widget=forms.CheckboxSelectMultiple)
    model = MultipleChoiceFilter(choices=get_choices(GPUSpecs, 'model'), widget=forms.CheckboxSelectMultiple)
    chipset = MultipleChoiceFilter(choices=get_choices(GPUSpecs, 'chipset'),
                                   widget=forms.CheckboxSelectMultiple)
    memory = MultipleChoiceFilter(choices=get_choices(GPUSpecs, 'memory'),
                                  widget=forms.CheckboxSelectMultiple)
    core_clock = MultipleChoiceFilter(choices=get_choices(GPUSpecs, 'core_clock'), widget=forms.CheckboxSelectMultiple)
    boost_clock = MultipleChoiceFilter(choices=get_choices(GPUSpecs, 'boost_clock'),
                                       widget=forms.CheckboxSelectMultiple)
    color = MultipleChoiceFilter(choices=get_choices(GPUSpecs, 'color'),
                                 widget=forms.CheckboxSelectMultiple)
    length = MultipleChoiceFilter(choices=get_choices(GPUSpecs, 'length'), widget=forms.CheckboxSelectMultiple)


class MBFilter(django_filters.FilterSet):
    brand = MultipleChoiceFilter(choices=get_choices(MBSpecs, 'brand'), widget=forms.CheckboxSelectMultiple)
    model = MultipleChoiceFilter(choices=get_choices(MBSpecs, 'model'), widget=forms.CheckboxSelectMultiple)
    socket = MultipleChoiceFilter(choices=get_choices(MBSpecs, 'socket'),
                                  widget=forms.CheckboxSelectMultiple)
    form_factor = MultipleChoiceFilter(choices=get_choices(MBSpecs, 'form_factor'),
                                       widget=forms.CheckboxSelectMultiple)
    mem_max = MultipleChoiceFilter(choices=get_choices(MBSpecs, 'mem_max'), widget=forms.CheckboxSelectMultiple)
    mem_slots = MultipleChoiceFilter(choices=get_choices(MBSpecs, 'mem_slots'),
                                     widget=forms.CheckboxSelectMultiple)
    color = MultipleChoiceFilter(choices=get_choices(MBSpecs, 'color'),
                                 widget=forms.CheckboxSelectMultiple)


class PSUFilter(django_filters.FilterSet):
    brand = MultipleChoiceFilter(choices=get_choices(PSUSpecs, 'brand'), widget=forms.CheckboxSelectMultiple)
    model = MultipleChoiceFilter(choices=get_choices(PSUSpecs, 'model'), widget=forms.CheckboxSelectMultiple)
    form_factor = MultipleChoiceFilter(choices=get_choices(PSUSpecs, 'form_factor'),
                                       widget=forms.CheckboxSelectMultiple)
    eff_rating = MultipleChoiceFilter(choices=get_choices(PSUSpecs, 'eff_rating'),
                                      widget=forms.CheckboxSelectMultiple)
    wattage = MultipleChoiceFilter(choices=get_choices(PSUSpecs, 'wattage'), widget=forms.CheckboxSelectMultiple)
    modular = MultipleChoiceFilter(choices=get_choices(PSUSpecs, 'modular'),
                                   widget=forms.CheckboxSelectMultiple)
    color = MultipleChoiceFilter(choices=get_choices(PSUSpecs, 'color'),
                                 widget=forms.CheckboxSelectMultiple)


class RAMFilter(django_filters.FilterSet):
    brand = MultipleChoiceFilter(choices=get_choices(RAMSpecs, 'brand'), widget=forms.CheckboxSelectMultiple)
    model = MultipleChoiceFilter(choices=get_choices(RAMSpecs, 'model'), widget=forms.CheckboxSelectMultiple)
    speed = MultipleChoiceFilter(choices=get_choices(RAMSpecs, 'speed'),
                                 widget=forms.CheckboxSelectMultiple)
    modules = MultipleChoiceFilter(choices=get_choices(RAMSpecs, 'modules'),
                                   widget=forms.CheckboxSelectMultiple)
    price_per_gb = MultipleChoiceFilter(choices=get_choices(RAMSpecs, 'price_per_gb'),
                                        widget=forms.CheckboxSelectMultiple)
    cas_lat = MultipleChoiceFilter(choices=get_choices(RAMSpecs, 'cas_lat'),
                                   widget=forms.CheckboxSelectMultiple)
    first_word_lat = MultipleChoiceFilter(choices=get_choices(RAMSpecs, 'first_word_lat'),
                                          widget=forms.CheckboxSelectMultiple)


class StorFilter(django_filters.FilterSet):
    brand = MultipleChoiceFilter(choices=get_choices(StorSpecs, 'brand'), widget=forms.CheckboxSelectMultiple)
    model = MultipleChoiceFilter(choices=get_choices(StorSpecs, 'model'), widget=forms.CheckboxSelectMultiple)
    capacity = MultipleChoiceFilter(choices=get_choices(StorSpecs, 'capacity'),
                                    widget=forms.CheckboxSelectMultiple)
    drive_type = MultipleChoiceFilter(choices=get_choices(StorSpecs, 'drive_type'),
                                      widget=forms.CheckboxSelectMultiple)
    cache = MultipleChoiceFilter(choices=get_choices(StorSpecs, 'cache'),
                                 widget=forms.CheckboxSelectMultiple)
    form_factor = MultipleChoiceFilter(choices=get_choices(StorSpecs, 'form_factor'),
                                       widget=forms.CheckboxSelectMultiple)
    interface = MultipleChoiceFilter(choices=get_choices(StorSpecs, 'interface'),
                                     widget=forms.CheckboxSelectMultiple)
    price_per_gb = MultipleChoiceFilter(choices=get_choices(StorSpecs, 'price_per_gb'),
                                        widget=forms.CheckboxSelectMultiple)

import django_tables2 as tables
from .models import MonitorSpecs, CPUSpecs, GPUSpecs, MBSpecs, PSUSpecs, RAMSpecs, StorSpecs
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import MonitorFilter


class MonitorTable(tables.Table):
    class Meta:
        model = MonitorSpecs
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("brand", "model", "size", "resolution", "ref_rate", "res_rate", "panel_type", "asp_ratio", "price",
                  "curved")


class CPUTable(tables.Table):
    class Meta:
        model = CPUSpecs
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("brand", "model", "core_count", "boost_clock", "tdp", "integrated_graphics", "smt", "core_clock",
                  "price")


class GPUTable(tables.Table):
    class Meta:
        model = GPUSpecs
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("brand", "model", "chipset", "memory", "core_clock", "boost_clock", "color", "length",
                  "price")


class MBTable(tables.Table):
    class Meta:
        model = MBSpecs
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("brand", "model", "socket", "form_factor", "mem_max", "mem_slots", "color",
                  "price")


class PSUTable(tables.Table):
    class Meta:
        model = PSUSpecs
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("brand", "model", "form_factor", "eff_rating", "wattage", "modular", "color",
                  "price")


class RAMTable(tables.Table):
    class Meta:
        model = RAMSpecs
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("brand", "model", "speed", "modules", "price_per_gb", "color", "cas_lat", "first_word_lat",
                  "price")


class StorTable(tables.Table):
    class Meta:
        model = StorSpecs
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("brand", "model", "capacity", "drive_type", "cache", "form_factor", "interface", "price_per_gb",
                  "price")

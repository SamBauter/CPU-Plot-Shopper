import django_tables2 as tables
from .models import MonitorSpecs
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import MonitorFilter


class MonitorTable(tables.Table):
    class Meta:
        model = MonitorSpecs
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("brand", "model", "size", "resolution", "ref_rate", "res_rate", "panel_type", "asp_ratio", "price",
                  "curved")


#class FilteredMonitorListView(SingleTableMixin, FilterView):
 #   table_class = MonitorTable
  #  model = MonitorSpecs
   # template_name = "django_tables2/bootstrap-responsive.html"
    #filterset_class = MonitorFilter

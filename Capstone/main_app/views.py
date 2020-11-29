from django.shortcuts import render
from .models import MonitorSpecs
from .tables import MonitorTable
from .filters import MonitorFilter
from django_tables2 import RequestConfig


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def dashboard_test(request):
    f=MonitorFilter(request.GET, queryset=MonitorSpecs.objects.all())
    monitor_fields = [f.name for f in MonitorSpecs._meta.get_fields()]
    monitor_fields.remove('id')
    monitor_fields.remove('model')
    monitor_fields.remove('price')
    sync_options = monitor_fields[-6:]
    monitor_fields = monitor_fields[:-6]
    monitor_fields.append('sync_options')

    brands = MonitorSpecs.objects.getUniqueValues('brand')
    resolutions = MonitorSpecs.objects.getUniqueValues('resolution')
    sizes = MonitorSpecs.objects.getUniqueValues('size')
    ref_rates = MonitorSpecs.objects.getUniqueValues('ref_rate')
    res_rates = MonitorSpecs.objects.getUniqueValues('res_rate')
    panel_types = MonitorSpecs.objects.getUniqueValues('panel_type')
    asp_ratios = MonitorSpecs.objects.getUniqueValues('asp_ratio')
    curved_options = ['Curved', 'Not Curved']
    all_options = [brands, resolutions, sizes, ref_rates, res_rates, panel_types, asp_ratios, curved_options,
                   sync_options]

    filter_dict = {monitor_fields[i]: all_options[i] for i in range(len(monitor_fields))}

    table = MonitorTable(f.qs)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get("page", 1), per_page=25)

    return render(request, 'dashboard_test.html', {'filter_dict': filter_dict,
                                                   'table': table,
                                                   'filter': f})

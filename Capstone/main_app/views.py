from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import MonitorSpecs
from .filters import MonitorFilter
from .tables import MonitorTable


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def dashboard_test(request):
    f = MonitorFilter(request.GET, queryset=MonitorSpecs.objects.all())
    # monitor_fields = [f.name for f in MonitorSpecs._meta.get_fields()]
    # monitor_fields.remove('id')
    # monitor_fields.remove('model')
    # monitor_fields.remove('price')

    # brands = MonitorSpecs.objects.getUniqueValues('brand')
    # resolutions = MonitorSpecs.objects.getUniqueValues('resolution')
    # sizes = MonitorSpecs.objects.getUniqueValues('size')
    # ref_rates = MonitorSpecs.objects.getUniqueValues('ref_rate')
    # res_rates = MonitorSpecs.objects.getUniqueValues('res_rate')
    # panel_types = MonitorSpecs.objects.getUniqueValues('panel_type')
    # asp_ratios = MonitorSpecs.objects.getUniqueValues('asp_ratio')
    # curved_options = ['Curved', 'Not Curved']
    # g_sync_compat_options = ['True', 'False']
    # sync_options = ['G Sync', 'G Sync Ultimate', 'Free Sync', 'Free Sync Premium', 'Free Sync Premium Pro']
    # all_options = [brands, sizes, resolutions, ref_rates, res_rates, panel_types, asp_ratios, curved_options, g_sync_compat_options,
    #              sync_options]

    # filter_dict = {monitor_fields[i]: all_options[i] for i in range(len(monitor_fields))}

    table = MonitorTable(f.qs)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get("page", 1), per_page=25)

    return render(request, 'dashboard_test.html', {
        'table': table,
        'filter': f})

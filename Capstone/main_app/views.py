from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import MonitorSpecs
from .filters import MonitorFilter
from .tables import MonitorTable
from .graphs import MonitorGraph


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def dashboard_test(request):
    f = MonitorFilter(request.GET, queryset=MonitorSpecs.objects.filter(price__isnull=False))

    table = MonitorTable(f.qs)
    graph = MonitorGraph(f.qs)
    graph_html = graph.get_html_graph()
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get("page", 1), per_page=25)

    return render(request, 'dashboard_test.html', {
        'table': table,
        'filter': f,
        'graph_html': graph_html})

#def monitor_graph(request):

#def cpu_graph(request):

#def gpu_graph(request):

#def motherboard_graph(request):

#def ram_graph(request):

#def stor_graph(request):


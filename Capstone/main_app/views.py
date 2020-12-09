from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from .models import MonitorSpecs, CPUSpecs, GPUSpecs, MBSpecs, PSUSpecs, RAMSpecs, StorSpecs
from .models import db_counts
from .filters import MonitorFilter, CPUFilter, GPUFilter, MBFilter, PSUFilter, RAMFilter, StorFilter
from .tables import MonitorTable, CPUTable, GPUTable, MBTable, PSUTable, RAMTable, StorTable
from .graphs import CategoryGraph
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {
        'db_counts': db_counts
    })


def dashboard(request):
    return render(request, 'dashboard.html')


def monitor_graph(request):
    f = MonitorFilter(request.GET, queryset=MonitorSpecs.objects.filter(price__isnull=False))
    if f.qs:
        table = MonitorTable(f.qs)
        graph = CategoryGraph(f.qs, x='price', y='size', title='Monitors by Size and Price', x_label='Price ($)',
                              y_label='Size (inches)')
        graph_html = graph.get_html_graph()
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=25)

        return render(request, 'dashboard_test.html', {
            'title': 'Monitors',
            'table_title': 'Monitors',
            'table': table,
            'filter': f,
            'graph_html': graph_html})
    else:
        messages.error(request, 'No products found with selected filter options please try a broader search')
        return redirect('/monitor_graph')


def cpu_graph(request):
    f = CPUFilter(request.GET, queryset=CPUSpecs.objects.filter(price__isnull=False))
    if f.qs:
        table = CPUTable(f.qs)
        graph = CategoryGraph(f.qs, x='price', y='core_clock', title='CPUS by Core Clock and Price',
                              x_label='Price ($)',
                              y_label='Core Clock (GHz)')
        graph_html = graph.get_html_graph()
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return render(request, 'dashboard_test.html', {
            'title': 'CPUs',
            'table_title': 'CPUs',
            'table': table,
            'filter': f,
            'graph_html': graph_html})
    else:
        messages.error(request, 'No products found with selected filter options please try a broader search')
        return redirect('/cpu_graph')


def gpu_graph(request):
    f = GPUFilter(request.GET, queryset=GPUSpecs.objects.filter(price__isnull=False))
    if f.qs:
        table = GPUTable(f.qs)
        graph = CategoryGraph(f.qs, x='price', y='memory', title='GPUs by Memory and Price', x_label='Price ($)',
                              y_label='Memory (GB)')
        graph_html = graph.get_html_graph()
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return render(request, 'dashboard_test.html', {
            'title': 'GPUs',
            'table_title': 'GPUs',
            'table': table,
            'filter': f,
            'graph_html': graph_html})
    else:
        messages.error(request, 'No products found with selected filter options please try a broader search')
        return redirect('/gpu_graph')


def motherboard_graph(request):
    f = MBFilter(request.GET, queryset=MBSpecs.objects.filter(price__isnull=False))
    if f.qs:
        table = MBTable(f.qs)
        graph = CategoryGraph(f.qs, x='price', y='mem_max', title='Motherboards by Memory Max and Price',
                              x_label='Price ($)',
                              y_label='Memory Maximum (GB)')
        graph_html = graph.get_html_graph()
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return render(request, 'dashboard_test.html', {
            'title': 'MotherBoards',
            'table_title': 'MotherBoards',
            'table': table,
            'filter': f,
            'graph_html': graph_html})
    else:
        messages.error(request, 'No products found with selected filter options please try a broader search')
        return redirect('/motherboard_graph')


def psu_graph(request):
    f = PSUFilter(request.GET, queryset=PSUSpecs.objects.filter(price__isnull=False))
    if f.qs:
        table = PSUTable(f.qs)
        graph = CategoryGraph(f.qs, x='price', y='wattage', title='PSUs by Wattage and Price',
                              x_label='Price ($)',
                              y_label='Watts (W)')
        graph_html = graph.get_html_graph()
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return render(request, 'dashboard_test.html', {
            'title': 'PSUs',
            'table_title': 'PSUs',
            'table': table,
            'filter': f,
            'graph_html': graph_html})
    else:
        messages.error(request, 'No products found with selected filter options please try a broader search')
        return redirect('/psu_graph')


def ram_graph(request):
    qs = RAMSpecs.objects.filter(price_per_gb__isnull=False)
    f = RAMFilter(request.GET, queryset=qs.filter(price__isnull=False))
    if f.qs:
        table = RAMTable(f.qs)
        graph = CategoryGraph(f.qs, x='price', y='price_per_gb', title='RAM by Price Per GB and Price',
                              x_label='Price ($)',
                              y_label='Price Per GB ($)')
        graph_html = graph.get_html_graph()
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return render(request, 'dashboard_test.html', {
            'title': 'RAM',
            'table_title': 'RAMs',
            'table': table,
            'filter': f,
            'graph_html': graph_html})
    else:
        messages.error(request, 'No products found with selected filter options please try a broader search')
        return redirect('/ram_graph')


def stor_graph(request):
    qs = StorSpecs.objects.filter(price_per_gb__isnull=False)
    f = StorFilter(request.GET, queryset=qs.filter(price__isnull=False))
    if f.qs:
        table = StorTable(f.qs)
        graph = CategoryGraph(f.qs, x='price', y='price_per_gb', title='Storage by Price Per GB and Price',
                              x_label='Price ($)',
                              y_label='Price Per GB ($)')
        graph_html = graph.get_html_graph()
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return render(request, 'dashboard_test.html', {
            'title': 'Storage',
            'table_title': 'Storage',
            'table': table,
            'filter': f,
            'graph_html': graph_html})
    else:
        messages.error(request, 'No products found with selected filter options please try a broader search')
        return redirect('/stor_graph')


def login_register(request):
    if request.method == 'POST':
        email = request.POST.get('username_email')
        password = request.POST.get('password')
        if not email or not password:
            messages.info(request, 'Please fill out all fields')
            return redirect('/')
        elif 'login_btn' in request.POST:
            print('Login HIT')
            user = auth.authenticate(username=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Email or Password')
                return redirect('/')

        elif 'sign_up_btn' in request.POST:
            if User.objects.filter(username=email).exists():
                messages.error(request, 'User already exists')
                return redirect('/')
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                messages.success(request, 'Sign Up Successful')
                return redirect('/')
        else:
            return redirect('/')
    else:
        messages.info(request, 'Enter Login Information')
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


def list_all(request, **kwargs):
    category = kwargs['category']
    back_url = '/'+category
    print('CATEGORY' + category)
    cat_split = category.split('_')
    cat_name = cat_split[0].capitalize() + 's'
    print('CATEGORY_NAME' + cat_name)

    print(category)
    if category == 'monitor_graph':
        f = MonitorFilter(request.GET, MonitorSpecs.objects.all())
        t = MonitorTable(f.qs)
    elif category == 'cpu_graph':
        f = CPUFilter(request.GET, CPUSpecs.objects.all())
        t = CPUTable(f.qs)
    elif category == 'gpu_graph':
        f = GPUFilter(request.GET, GPUSpecs.objects.all())
        t = GPUTable(f.qs)
    elif category == 'motherboard_graph':
        f = MBFilter(request.GET, MBSpecs.objects.all())
        t = MBTable(f.qs)
    elif category == 'psu_graph':
        f = PSUFilter(request.GET, PSUSpecs.objects.all())
        t = PSUTable(f.qs)
    elif category == 'ram_graph':
        f = RAMFilter(request.GET, RAMSpecs.objects.all())
        t = RAMTable(f.qs)
    else:
        f = StorFilter(request.GET, StorSpecs.objects.all())
        t = StorTable(f.qs)

    RequestConfig(request).configure(t)
    t.paginate(page=request.GET.get("page", 1), per_page=25)

    return render(request, 'list_all.html', {
        'title': cat_name,
        'table': t,
        'filter': f,
        'back_url': back_url
    })

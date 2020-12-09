from . import views
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^$', views.index),
    path('index/', views.index),
    path('dashboard/', views.dashboard),
    path('monitor_graph/', views.monitor_graph),
    path('cpu_graph/', views.cpu_graph),
    path('gpu_graph/', views.gpu_graph),
    path('motherboard_graph/', views.motherboard_graph),
    path('psu_graph/', views.psu_graph),
    path('ram_graph/', views.ram_graph),
    path('stor_graph', views.stor_graph),
    path('login_register/', views.login_register),
    path('logout/', views.logout)
]

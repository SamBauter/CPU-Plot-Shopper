from . import views
from django.urls import path,re_path
urlpatterns = [
    re_path(r'^$', views.index),
    path('index/',views.index),
    path('dashboard/', views.dashboard),
    path('dashboard_test/', views.dashboard_test)


]
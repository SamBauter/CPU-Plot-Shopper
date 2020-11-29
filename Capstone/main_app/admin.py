from django.contrib import admin
from .models import MonitorSpecs,CPUSpecs,GPUSpecs,StorSpecs,RAMSpecs,PSUSpecs,MBSpecs
# Register your models here.

admin.site.register(MonitorSpecs)
admin.site.register(MBSpecs)
admin.site.register(CPUSpecs)
admin.site.register(GPUSpecs)
admin.site.register(StorSpecs)
admin.site.register(RAMSpecs)
admin.site.register(PSUSpecs)



from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin

from .models import Worker, WorkerMonitorLog


# Register your models here.
@admin.register(Worker)
class WorkerAdmin(SafeDeleteAdmin):
    list_display = [field.name for field in Worker._meta.fields]
    list_filter = ["deleted"]


@admin.register(WorkerMonitorLog)
class WorkerMonitorLogAdmin(SafeDeleteAdmin):
    list_display = [field.name for field in WorkerMonitorLog._meta.fields]
    list_filter = ["deleted"]

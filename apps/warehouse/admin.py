from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin

from .models import Organization, Package, Domain


# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(SafeDeleteAdmin):
    list_display = [field.name for field in Organization._meta.fields]
    list_filter = ["deleted"]


@admin.register(Package)
class PackageAdmin(SafeDeleteAdmin):
    list_display = [field.name for field in Package._meta.fields]
    list_filter = ["deleted"]


@admin.register(Domain)
class ModelNameAdmin(SafeDeleteAdmin):
    list_display = [field.name for field in Domain._meta.fields]
    list_filter = ["deleted"]

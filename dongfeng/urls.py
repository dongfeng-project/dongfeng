"""
URL configuration for dongfeng project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.overwatch.views import WorkerViewSet, WorkerMonitorLogViewSet, WorkerMonitorLogCleanupView
from apps.spaceport.views import UserLoginView, CurrentUserView
from apps.warehouse.views import OrgViewSet, PackageViewSet, DomainViewSet, GenericIPViewSet
from dongfeng import settings

router = routers.DefaultRouter()
router.register(prefix=r"worker", viewset=WorkerViewSet, basename="worker")
router.register(prefix=r"worker-monitor-log", viewset=WorkerMonitorLogViewSet, basename="worker-monitor-log")
router.register(prefix=r"organization", viewset=OrgViewSet, basename="org")
router.register(prefix=r"package", viewset=PackageViewSet, basename="pkg")
router.register(prefix=r"domain", viewset=DomainViewSet, basename="domain")
router.register(prefix=r"ip", viewset=GenericIPViewSet, basename="ip")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/current-user/", CurrentUserView.as_view(), name="current-user"),
    path("api/login/", UserLoginView.as_view(), name="login"),
    path("api/worker-monitor-log-cleanup/", WorkerMonitorLogCleanupView.as_view(), name="worker-monitor-log-cleanup"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__", include("debug_toolbar.urls")))

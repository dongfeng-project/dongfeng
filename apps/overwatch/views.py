from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers


# Create your views here.
class WorkerViewSet(viewsets.ModelViewSet):
    queryset = models.Worker.objects.all().order_by("-updated")
    serializer_class = serializers.WorkerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (SessionAuthentication, TokenAuthentication)


class WorkerMonitorLogViewSet(viewsets.ModelViewSet):
    queryset = models.WorkerMonitorLog.objects.select_related("worker").all().order_by("-created")
    serializer_class = serializers.WorkerMonitorLogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (SessionAuthentication, TokenAuthentication)

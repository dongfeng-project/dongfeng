from datetime import timedelta

from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

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


class WorkerMonitorLogCleanupView(GenericAPIView):
    def get_queryset(self):
        days = int(self.request.query_params.get("days", 30))
        return models.WorkerMonitorLog.objects.filter(created__lte=timezone.now() - timedelta(days=days))

    def delete(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        cnt, _ = queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"deleted": cnt})

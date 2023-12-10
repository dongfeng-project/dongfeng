from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializers, models


# Create your views here.
class OrgViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrgSerializer
    queryset = models.Organization.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class PackageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PkgSerializer
    queryset = models.Package.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class DomainViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DomainSerializer
    queryset = models.Domain.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class GenericIPViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GenericIPSerializer
    queryset = models.GenericIP.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

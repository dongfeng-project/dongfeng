from . import models

from rest_framework import serializers


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = "__all__"


class PkgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Package
        fields = "__all__"


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Domain
        fields = "__all__"


class GenericIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GenericIP
        fields = "__all__"

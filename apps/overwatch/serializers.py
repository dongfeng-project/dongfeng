from rest_framework import serializers

from . import models


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Worker
        fields = "__all__"
        read_only_fields = ("id", "created", "updated")


class WorkerMonitorLogSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer()

    def create(self, validated_data):
        worker_data = validated_data.pop("worker")
        worker, _ = models.Worker.objects.update_or_create(name=worker_data["name"], defaults=worker_data)
        worker_log = models.WorkerMonitorLog.objects.create(worker=worker, **validated_data)
        return worker_log

    class Meta:
        model = models.WorkerMonitorLog
        fields = "__all__"
        read_only_fields = ("id", "created", "updated")

from enum import Enum

from django.db import models


class CeleryTaskName(Enum):
    OVERWATCH_RESOURCE_USAGE = "overwatch.resource_usage"
    OVERWATCH_GET_WORKER_STATS = "overwatch.get_worker_stats"


class TaskStatus(models.IntegerChoices):
    PENDING = 0, "等待中"
    RUNNING = 1, "运行中"
    EXCEPTION = 2, "异常"
    DONE = 3, "完成"

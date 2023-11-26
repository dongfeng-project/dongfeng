from enum import Enum

from django.db import models


class CeleryTaskName(Enum):
    # overwatch - for worker monitor
    OVERWATCH_RESOURCE_USAGE = "overwatch.resource_usage"
    OVERWATCH_GET_WORKER_STATS = "overwatch.get_worker_stats"
    OVERWATCH_REPORT_WORKER_MONITOR_LOG = "overwatch.report_worker_monitor_log"
    OVERWATCH_WORKER_MONITOR_LOG_CLEANUP = "overwatch.worker_monitor_log_cleanup"

    # scout - for service discover
    SCOUT_NMAP_DETECT_UP_HOST = "scout.nmap_detect_up_host"


class TaskStatus(models.IntegerChoices):
    PENDING = 0, "等待中"
    RUNNING = 1, "运行中"
    EXCEPTION = 2, "异常"
    DONE = 3, "完成"

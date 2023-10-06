import os

from celery import Celery
from kombu.serialization import registry

from consts.task import CeleryTaskName
from .settings import CELERY_SERIALIZER, CELERY_RESULT_SERIALIZER, CELERY_ACCEPT_CONTENT

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dongfeng.settings")

app = Celery("dongfeng")
# https://github.com/celery/celery/issues/5075
registry.enable("pickle")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.task_serializer = CELERY_SERIALIZER
app.conf.result_serializer = CELERY_RESULT_SERIALIZER
app.conf.accept_content = CELERY_ACCEPT_CONTENT

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app.autodiscover_tasks(packages=["tasks"])

# celery beat
app.conf.beat_schedule = {
    "get_worker_stats": {
        "task": CeleryTaskName.OVERWATCH_GET_WORKER_STATS.value,
        "schedule": 30,
    }
}

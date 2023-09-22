import os
import socket
import time

import psutil
from celery import shared_task
from celery.utils.log import get_task_logger
from celery.worker.control import inspect_command

from consts.task import CeleryTaskName
from dongfeng.celery import app
from entities.task import ResourceUsageResult
from utils import api
from utils.ip import get_local_ip

logger = get_task_logger(__name__)


@shared_task(name=CeleryTaskName.OVERWATCH_GET_WORKER_STATS.value)
def get_worker_stats():
    """
    Get resource usage data of all workers.
    :return:
    """
    results = app.control.broadcast(CeleryTaskName.OVERWATCH_RESOURCE_USAGE.value, reply=True, timeout=5)
    for worker_stat_json in results:
        for hostname in worker_stat_json:
            r: ResourceUsageResult = worker_stat_json[hostname]
            logger.info(f"get worker [{hostname}] resource usage {r}")
            api.report_worker_monitor_log(
                name=r.name,
                ip=r.ip,
                hostname=r.hostname,
                uptime=r.uptime,
                cpu=r.cpu,
                worker_cpu=r.worker_cpu,
                mem=r.mem,
                worker_mem=r.worker_mem,
                worker_threads=r.worker_threads,
            )


@inspect_command(name=CeleryTaskName.OVERWATCH_RESOURCE_USAGE.value)
def resource_usage(state) -> ResourceUsageResult:
    p = psutil.Process(os.getpid())
    with p.oneshot():
        worker_cpu = p.cpu_percent(interval=1)
        worker_mem = p.memory_info().rss / 1024 / 1024
        agent_threads = p.num_threads()

    uptime = time.time() - psutil.boot_time()
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    result = ResourceUsageResult(
        name=state.consumer.hostname,
        ip=get_local_ip(),
        hostname=socket.gethostname(),
        uptime=uptime,
        cpu=cpu,
        worker_cpu=worker_cpu,
        mem=mem,
        worker_mem=worker_mem,
        worker_threads=agent_threads,
    )
    return result

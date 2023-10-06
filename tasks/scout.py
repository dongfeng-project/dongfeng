from celery import shared_task

from agents import nmap
from consts.task import CeleryTaskName
from entities.task import UpHostResult


@shared_task(name=CeleryTaskName.SCOUT_NMAP_DETECT_UP_HOST.value)
def nmap_detect_up_hosts(ips: str) -> UpHostResult:
    return nmap.detect_host(ips=ips)

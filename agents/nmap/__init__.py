import nmap
from celery.utils.log import get_task_logger

from entities.task import UpHostResult
from utils.ip import parse_ips

logger = get_task_logger(__name__)


def detect_host(ips: str) -> UpHostResult:
    """

    :param ips:
    :return:
    """
    target_list = parse_ips(ips)
    up_hosts = []
    nm = nmap.PortScanner()
    for target in target_list:
        nm.scan(hosts=str(target), ports=None, arguments="-n -sn -PE --min-hostgroup 512 --min-parallelism 512")
        logger.debug(nm.command_line())
        up_hosts.extend(nm.all_hosts())

    result = UpHostResult(up_hosts=up_hosts)
    return result

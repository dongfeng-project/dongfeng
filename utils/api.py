import logging
from urllib.parse import urljoin

from rest_framework.reverse import reverse
from rest_framework.test import RequestsClient

from dongfeng.settings import TOKEN

client = RequestsClient()
logger = logging.getLogger(__name__)


def send_req(method: str, url: str, data: dict = None, headers: dict = None, base_url: str = "http://testserver/"):
    """
    HTTP request method.
    :param method: HTTP method
    :param url: relative URL
    :param data: POST body, JSON
    :param headers: HTTP request headers
    :param base_url:
    :return:
    """
    if headers is None:
        headers = {"Authorization": f"Token {TOKEN}"}
    else:
        headers = headers

    if url.startswith("http"):
        logger.error(f"relative URL needed")
        return None
    else:
        abs_url = urljoin(base=base_url, url=url)

    if not abs_url.endswith("/"):
        abs_url += "/"

    if method.lower() == "get":
        return client.get(url=abs_url, headers=headers)
    elif method.lower() == "post":
        return client.post(url=abs_url, json=data, headers=headers)
    elif method.lower() == "patch":
        return client.patch(url=abs_url, json=data, headers=headers)
    else:
        logger.error(f"unsupported HTTP method {method}")
        return None


def report_worker_monitor_log(
    name: str,
    ip: str,
    hostname: str,
    uptime: float,
    cpu: float,
    worker_cpu: float,
    mem: float,
    worker_mem: float,
    worker_threads: int,
) -> None:
    """
    Report worker monitor logs.
    :param name:
    :param ip:
    :param hostname:
    :param uptime:
    :param cpu:
    :param worker_cpu:
    :param mem:
    :param worker_mem:
    :param worker_threads:
    :return:
    """
    req = send_req(
        method="post",
        url=reverse(viewname="worker-monitor-log-list"),
        data={
            "uptime": int(uptime),
            "cpu": cpu,
            "worker_cpu": worker_cpu,
            "mem": mem,
            "worker_mem": worker_mem,
            "worker_threads": worker_threads,
            "worker": {"name": name, "hostname": hostname, "ip": ip},
        },
    )
    try:
        result = req.json()
        if result.get("success") is True:
            logger.info(f"report worker [{name}] monitor log success")
        else:
            logger.error(f"report worker [{name}] monitor log error, {result.get('msg')}")
    except Exception as e:
        logger.error(f"report worker monitor log failed {e}, response {req.text}")

import logging
from urllib.parse import urljoin

import httpx
from rest_framework.reverse import reverse

from dongfeng.settings import TOKEN, API_HOST, API_HTTPS
from exceptions.task import HTTPException

client = httpx.Client()
logger = logging.getLogger(__name__)


def get_api_base_url(host: str, https: bool = False):
    """
    Generate API base URL.
    :param host:
    :param https:
    :return:
    """
    return f"http{'s' if https else ''}://{host}/"


def send_req(method: str, url: str, params: dict = None, data: dict = None, headers: dict = None, base_url: str = None):
    """
    HTTP request method.
    :param method: HTTP method
    :param url: relative URL
    :param params:GET params
    :param data: POST body, JSON
    :param headers: HTTP request headers
    :param base_url:
    :return:
    """
    if not base_url:
        base_url = get_api_base_url(host=API_HOST, https=API_HTTPS)

    if headers is None:
        headers = {"Authorization": f"Token {TOKEN}"}
    else:
        headers = headers

    if url.startswith("http"):
        raise HTTPException(f"relative URL needed")
    else:
        abs_url = urljoin(base=base_url, url=url)

    if not abs_url.endswith("/"):
        abs_url += "/"

    if method.lower() in ("get", "post", "patch", "delete"):
        try:
            return client.request(method=method.lower(), url=abs_url, params=params, json=data, headers=headers)
        except Exception as e:
            raise HTTPException(f"send req failed: {e}")
    else:
        raise HTTPException(f"unsupported HTTP method {method}")


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

    try:
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

        result = req.json()
        if result.get("success") is True:
            logger.info(f"report worker [{name}] monitor log success")
        else:
            logger.error(f"report worker [{name}] monitor log error, {result.get('msg')}")
    except HTTPException as e:
        logger.error(f"request failed while reporting worker monitor log {e}")
    except Exception as e:
        logger.error(f"report worker monitor log failed {e}")

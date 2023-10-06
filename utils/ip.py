import ipaddress
import socket
from json import JSONDecodeError
from typing import List

import httpx
from celery.utils.log import get_task_logger

from exceptions.task import InvalidIP

logger = get_task_logger(__name__)


def get_local_ip() -> str:
    """
    获取本机ip
    :return: ip
    """
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as e:
        logger.error(f"get local ip address error {e}", exc_info=True)
        return ""


def is_private_ip(ip: str) -> bool:
    """
    判断是否内网ip
    :param ip:
    :return: Bool
    """
    try:
        ip = ipaddress.ip_address(ip.strip())
        return ip.is_private
    except ValueError:
        return False


def is_ip(ip: str) -> bool:
    """
    判断是否ip
    :param ip:
    :return:
    """
    try:
        ipaddress.ip_address(ip.strip())
        return True
    except ValueError:
        return False


def is_cidr(cidr: str) -> bool:
    """
    判断是否CIDR
    :param cidr:
    :return:
    """
    try:
        ipaddress.ip_network(cidr.strip())
        return True
    except ValueError:
        return False


def ip_geo_location(ip: str) -> str:
    """
    获取IP地理位置
    :param ip:
    :return:
    """
    if not is_ip(ip):
        raise InvalidIP(f"Invalid IP {ip}")

    try:
        req = httpx.get(url=f"https://ipinfo.io/{ip}/json", timeout=3)
        if req.status_code == 200:
            try:
                result = req.json()
                return f"{result['country']}/{result['region']}/{result['city']}"
            except JSONDecodeError:
                logger.error(f"query ip geo location error: {req.text}")
                return ""
        else:
            logger.error(f"query ip geo location error: {req.text}")
            return ""
    except Exception as e:
        logger.exception(f"query ip geo location failed: {e}")
        return ""


def parse_ips(ips: str) -> List[ipaddress.ip_network]:
    """
    Parse ip string to CIDR /16.
    :param ips:
    :return:
    """
    ip_list = []

    # IP range
    if "-" in ips:
        start_ip_str, end_ip_str = ips.split("-")[:2]
        if not is_ip(start_ip_str) or not is_ip(end_ip_str):
            raise InvalidIP(f"Invalid ip range {ips}")

        start_ip = ipaddress.ip_address(start_ip_str)
        end_ip = ipaddress.ip_address(end_ip_str)
        ip_list.extend([ipaddress.ip_address(int_ip) for int_ip in range(int(start_ip), int(end_ip) + 1)])
    # CIDR
    elif "/" in ips:
        if not is_cidr(ips):
            raise InvalidIP(f"Invalid CIDR {ips}")

        cidr_network = ipaddress.ip_network(ips)

        ip_list.extend(list(cidr_network.hosts()))
    else:
        if not is_ip(ips):
            raise InvalidIP(f"Invalid ip {ips}")

        ip_list.append(ipaddress.ip_address(ips))

    ip_list = list(set(ip_list))
    start_ip = min(ip_list)
    end_ip = max(ip_list)

    cidr_list = []
    for addr in ipaddress.summarize_address_range(start_ip, end_ip):
        try:
            cidr_list.extend(addr.subnets(new_prefix=16))
        except ValueError:
            cidr_list.append(addr)

    return cidr_list

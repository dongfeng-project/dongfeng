import socket

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


def get_local_ip() -> str:
    """
    获取本机ip
    :return: ip
    """
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as e:
        logger.error(f"获取本机IP异常 {e}", exc_info=True)
        return ""

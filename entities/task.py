from dataclasses import dataclass
from typing import List


@dataclass
class ResourceUsageResult:
    name: str
    ip: str
    hostname: str
    uptime: float
    cpu: float
    worker_cpu: float
    mem: float
    worker_mem: float
    worker_threads: int


@dataclass
class UpHostResult:
    up_hosts: List[str]

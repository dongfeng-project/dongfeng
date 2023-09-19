from dataclasses import dataclass


@dataclass
class ResourceUsageResult:
    ip: str
    hostname: str
    uptime: float
    cpu: float
    worker_cpu: float
    mem: float
    worker_mem: float
    worker_threads: int

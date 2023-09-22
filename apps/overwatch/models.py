from django.db import models

from utils.models import BaseModel


# Create your models here.
class Worker(BaseModel):
    name = models.CharField(verbose_name="名称", max_length=512, db_index=True)
    hostname = models.CharField(verbose_name="主机名", max_length=512, db_index=True)
    ip = models.GenericIPAddressField(verbose_name="IP")

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = "节点"
        verbose_name_plural = verbose_name


class WorkerMonitorLog(BaseModel):
    worker = models.ForeignKey(
        verbose_name="节点", to=Worker, on_delete=models.CASCADE, related_name="monitor_logs", db_constraint=False
    )
    uptime = models.PositiveBigIntegerField(verbose_name="启动时长")
    cpu = models.FloatField(verbose_name="系统CPU")
    worker_cpu = models.FloatField(verbose_name="进程CPU")
    mem = models.FloatField(verbose_name="内存占用")
    worker_mem = models.FloatField(verbose_name="进程内存占用")
    worker_threads = models.PositiveIntegerField(verbose_name="线程数")

    class Meta:
        verbose_name = "节点监控日志"
        verbose_name_plural = verbose_name

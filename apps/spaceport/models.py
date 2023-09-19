from django.db import models

from consts.task import TaskStatus
from utils.models import BaseModel


# Create your models here.
class Project(BaseModel):
    """
    项目
    """

    name = models.CharField(verbose_name="名称", max_length=128, db_index=True)
    desc = models.TextField(verbose_name="描述")

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name


class Task(BaseModel):
    """
    任务
    """

    project = models.ForeignKey(to=Project, verbose_name="项目", on_delete=models.CASCADE)
    type = models.CharField(verbose_name="类型", max_length=32, db_index=True)
    status = models.PositiveSmallIntegerField(
        verbose_name="状态", db_index=True, choices=TaskStatus.choices, default=TaskStatus.PENDING.value
    )
    info = models.TextField(verbose_name="内容", default="")

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = verbose_name


class Setting(BaseModel):
    name = models.CharField(verbose_name="名称", max_length=128, db_index=True)
    value = models.TextField(verbose_name="值")
    env = models.CharField(verbose_name="生效环境", max_length=64)

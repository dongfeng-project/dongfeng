from django.db import models

from consts import asset
from utils.models import BaseModel


# Create your models here.
class Organization(BaseModel):
    name = models.CharField(verbose_name="名称", max_length=1024, db_index=True)

    class Meta:
        verbose_name = "组织"
        verbose_name_plural = verbose_name


class Package(BaseModel):
    namespace = models.CharField(verbose_name="命名空间", max_length=1024, db_index=True)
    name = models.CharField(verbose_name="名称", max_length=1024, db_index=True)
    version = models.CharField(verbose_name="版本", max_length=1024, db_index=True)
    lang = models.CharField(verbose_name="语言", max_length=128, db_index=True)
    publish_time = models.DateTimeField(verbose_name="发布时间", db_index=True)
    tag = models.CharField(verbose_name="标签", max_length=128, db_index=True)
    author = models.CharField(verbose_name="作者", max_length=256, db_index=True)
    org = models.ForeignKey(
        verbose_name="组织", to=Organization, on_delete=models.SET_NULL, db_constraint=False, db_index=True, null=True
    )

    class Meta:
        verbose_name = "依赖包"
        verbose_name_plural = verbose_name


class Domain(BaseModel):
    domain = models.CharField(verbose_name="域名", max_length=512, db_index=True)
    dest = models.CharField(verbose_name="解析记录", max_length=1024, db_index=True)
    org = models.ForeignKey(
        verbose_name="组织", to=Organization, on_delete=models.SET_NULL, db_constraint=False, db_index=True, null=True
    )

    class Meta:
        verbose_name = "域名"
        verbose_name_plural = verbose_name


class GenericIP(BaseModel):
    name = models.CharField(verbose_name="名称", max_length=1024, db_index=True)
    hostname = models.CharField(verbose_name="主机名", max_length=1024, db_index=True, blank=True, default="")
    ip = models.GenericIPAddressField(verbose_name="IP", db_index=True)
    ip_type = models.CharField(verbose_name="IP类型", db_index=True, choices=asset.IPType.choices, max_length=32)
    org = models.ForeignKey(
        verbose_name="组织", to=Organization, on_delete=models.SET_NULL, db_constraint=False, db_index=True, null=True
    )

    class Meta:
        verbose_name = "物理机"
        verbose_name_plural = verbose_name

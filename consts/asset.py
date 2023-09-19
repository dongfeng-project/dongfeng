from django.db import models


class IPType(models.TextChoices):
    NODE = "node", "物理机"
    CONTAINER = "container", "容器"
    LB = "lb", "负载均衡"
    OTHER = "other", "其他"

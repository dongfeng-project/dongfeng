from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE


class BaseModel(SafeDeleteModel):
    """
    基础Model
    """

    _safedelete_policy = SOFT_DELETE_CASCADE

    created = CreationDateTimeField(verbose_name="创建时间")
    updated = ModificationDateTimeField(verbose_name="更新时间")

    class Meta:
        abstract = True

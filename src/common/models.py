from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ActiveModelQuerySet(models.QuerySet):

    def not_active(self, *args, **kwargs):
        return self.exclude(deleted_at=None, *args, **kwargs)

    def active(self, *args, **kwargs):
        return self.filter(deleted_at=None, *args, **kwargs)


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления", auto_now=True
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата удаления", blank=True, null=True, default=None
    )
    creator = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        default=None,
        null=True
    )

    objects = ActiveModelQuerySet().as_manager()

    class Meta:
        abstract = True

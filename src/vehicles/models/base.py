from django.db import models


class ActiveModelQuerySet(models.QuerySet):

    def not_active(self, *args, **kwargs):
        return self.filter(is_deleted=True, *args, **kwargs)

    def active(self, *args, **kwargs):
        return self.filter(is_deleted=False, *args, **kwargs)


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False, blank=True)
    objects = ActiveModelQuerySet().as_manager()

    class Meta:
        abstract = True

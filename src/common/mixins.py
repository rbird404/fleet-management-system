from rest_framework.mixins import DestroyModelMixin
from datetime import datetime


class DeactivateModelMixin(DestroyModelMixin):
    def perform_destroy(self, instance):
        instance.deleted_at = datetime.now()
        instance.save()

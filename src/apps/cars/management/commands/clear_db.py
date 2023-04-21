from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    def handle(self, *args, **options):
        app = apps.get_app_config('cars')
        for model in app.models.values():
            model.objects.all().delete()

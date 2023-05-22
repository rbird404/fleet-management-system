from django.contrib import admin
from maintenance.models import Task, Record, Issue


admin.site.register(Task)
admin.site.register(Issue)
admin.site.register(Record)

from django.contrib import admin

from waybills.models import Waybill, Image, File

admin.site.register(Waybill)
admin.site.register(Image)
admin.site.register(File)

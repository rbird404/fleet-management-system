from django.contrib import admin

from vehicles.models import (
    Color, Counter, Vehicle,
    Passport, Engine, Expense,
    ExpenseType, FuelType, Subdivision, Distribution
)

admin.site.register(Vehicle)
admin.site.register(Counter)
admin.site.register(FuelType)
admin.site.register(Subdivision)
admin.site.register(Expense)
admin.site.register(ExpenseType)
admin.site.register(Passport)
admin.site.register(Engine)
admin.site.register(Distribution)
admin.site.register(Color)
admin.site.register(Color)

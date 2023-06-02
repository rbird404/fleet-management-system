from django.urls import path, include

urlpatterns = [
    path('vehicles/', include('vehicles.urls')),
    path('waybills/', include('waybills.urls')),
    path('fueling/', include('fueling.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('dashboard/', include('dashboard.urls'))
]

from django.urls import path, include

urlpatterns = [
    path('vehicles/', include('vehicles.urls')),
    path('services/', include('vehicle_service.urls')),
    path('storage/', include('storage.urls'))
]

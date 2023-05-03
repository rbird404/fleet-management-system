from django.urls import path, include

urlpatterns = [
    path('vehicles/', include('vehicles.urls')),
]
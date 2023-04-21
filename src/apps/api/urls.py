from django.urls import include, path
from apps.cars.urls import router as car_router

urlpatterns = [
    path("cars/", include("apps.cars.urls"))

]

from django.urls import path

from dashboard.views import (
    VehicleCountAPI, IssueCountAPI, VehicleTopCounterAPI, VehicleTopFuelingAPI,
    FuelCostAPI, CostPerKilometerAPI, TotalMileageAPI, ExpensesCostAPI,
    ServiceCostAPI
)


urlpatterns = [
    path('vehicles/', VehicleCountAPI.as_view()),
    path('issues/', IssueCountAPI.as_view()),
    path('vehicles/top-counter/', VehicleTopCounterAPI.as_view()),
    path('vehicles/top-fueling/', VehicleTopFuelingAPI.as_view()),
    path('fuel-costs/', FuelCostAPI.as_view()),
    path('vehicles/cost-per-kilometer/', CostPerKilometerAPI.as_view()),
    path('vehicles/total-millage/', TotalMileageAPI.as_view()),
    path('vehicles/expenses/', ExpensesCostAPI.as_view()),
    path('vehicles/services/', ServiceCostAPI.as_view()),
]

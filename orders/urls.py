from django.urls import path,include

urlpatterns = [
    path("website/api/", include("orders.website.urls")),
    path("dashboard/api/", include("orders.dashboard.urls")),
]
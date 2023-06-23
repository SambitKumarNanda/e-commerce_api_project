from django.urls import path, include

urlpatterns = [
    path("website/api/", include("reviews.website.urls")),
    path("app/api/", include("reviews.app.urls")),
]
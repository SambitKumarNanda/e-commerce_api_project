from django.urls import path, include

urlpatterns = [
    path("websites/api/", include('userprofile.website.urls')),
]
from django.urls import path
from .views import AppProductReviewModelCreateAPIView

urlpatterns = [
    path("app-product-review-create-api/", AppProductReviewModelCreateAPIView.as_view(), name="AppProductReviewModelCreateAPIView")
]
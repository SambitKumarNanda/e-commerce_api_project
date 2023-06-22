from django.urls import path
from .views import WebsiteUserWishListUpdateAPIView, WebsiteUserWishListRemoveAPIView, WebsiteUserWishListAPIView, \
    WebsiteUserCartListAPIView, WebsiteUserCartUpdateAPIView, WebsiteUserCartRemoveAPIView

urlpatterns = [
    path("add-to-wishlist/", WebsiteUserWishListUpdateAPIView.as_view(), name="WebsiteUserWishListUpdateAPIView"),
    path("remove-to-wishlist/", WebsiteUserWishListRemoveAPIView.as_view(), name="WebsiteUserWishListRemoveAPIView"),
    path("user-wishlist/", WebsiteUserWishListAPIView.as_view(), name="WebsiteUserWishListAPIView"),
    path("user-cart/", WebsiteUserCartListAPIView.as_view(), name="WebsiteUserCartListAPIView"),
    path("add-to-cart/", WebsiteUserCartUpdateAPIView.as_view(), name="WebsiteUserCartUpdateAPIView"),
    path("remove-from-cart/", WebsiteUserCartRemoveAPIView.as_view(), name="WebsiteUserCartRemoveAPIView"),
]
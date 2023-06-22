from rest_framework import serializers
from ..models import UserWishListModel, UserCartModel
from products.dashboard.serializers import DashboardProductMainModelListSerializer


class WebsiteUserWishListUpdateSerializer(serializers.ModelSerializer):
    product_code = serializers.CharField()

    class Meta:
        model = UserWishListModel
        fields = ["product_code"]


class WebsiteUserWishListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = UserWishListModel
        fields = "__all__"

    def get_products(self, obj):
        try:
            data = DashboardProductMainModelListSerializer(obj.product.all(), many=True).data
        except:
            data = []
        return data


class WebsiteUserCartUpdateSerializer(serializers.ModelSerializer):
    product_code = serializers.CharField()

    class Meta:
        model = UserCartModel
        fields = ["product_code"]


class WebsiteUserCartListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = UserCartModel
        fields = "__all__"

    def get_product(self, obj):
        try:
            data = DashboardProductMainModelListSerializer(obj.product.all(), many=True).data
        except:
            return data

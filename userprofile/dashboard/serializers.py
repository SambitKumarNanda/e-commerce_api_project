from rest_framework import serializers
from products.dashboard.serializers import DashboardProductMainModelListSerializer
from ..models import UserWishListModel, UserCartModel


class DashboardUserWishListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = UserWishListModel
        fields = "__all__"

    def get_products(self, obj):
        try:
            data = DashboardProductMainModelListSerializer(obj.products.all(), many=True).data
        except:
            data = []
        return data


class DashboardUserCartListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = UserCartModel
        fields = "__all__"

    def get_products(self, obj):
        try:
            data = DashboardProductMainModelListSerializer(obj.products.all(), many=True).data
        except:
            data = []
        return data
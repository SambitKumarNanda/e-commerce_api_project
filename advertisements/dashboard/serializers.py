from rest_framework import serializers
from ..models import AdvertisementBanner, AdvertisementModel

class AdvertisementBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementBanner
        fields = "__all__"
        
        
class AdvertisementModelSerializer(serializers.ModelSerializer): 
    banner = serializers.SerializerMethodField()
    class Meta:
        model=AdvertisementModel
        fields="__all__"
        
    def get_banner(self, obj):
        try:
            data = AdvertisementBannerSerializer(obj.banner.all(), many=True).data
        except e as Exception:
            data = []
        return data
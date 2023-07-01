from rest_framework import serializers
from ..models import AdvertisementBanner, AdvertisementModel

class AdvertisementBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementBanner
        fields = ["media"]
class AdvertisementModelSerializer(serializers.ModelSerializer): 
    banner = serializers.SerializerMethodField()
    class Meta:
        model=AdvertisementModel
        fields=['title', 'banner']
        
    def get_banner(self, obj):
        try:
            data = AdvertisementBannerSerializer(obj.banner.all(), many=True).data
        except e as Exception:
            data = []
        return data
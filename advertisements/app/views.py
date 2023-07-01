from .serializers import AdvertisementBannerSerializer, AdvertisementModelSerializer
from ..models import AdvertisementBanner, AdvertisementModel
from rest_framework import generics, status
from rest_framework.response import Response

class AdvertisementModelListAPIView(generics.ListAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementModelSerializer
    
        
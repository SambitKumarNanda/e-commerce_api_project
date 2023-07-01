from .serializers import AdvertisementBannerSerializer, AdvertisementModelSerializer
from ..models import AdvertisementBanner, AdvertisementModel
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

class AdvertisementBannerModelCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    
    queryset = AdvertisementBanner.objects.all()
    serializer_class = AdvertisementBannerSerializer
    
    
class AdvertisementModelCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementModelSerializer
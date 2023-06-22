from products.dashboard.serializers import ProductModelListSerializer
from ..models import ProductModel
from rest_framework import serializers, status, generics
from rest_framework.response import Response
import django_filters
from ..filters import ProductFilter


class AppProductModelListAPIView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ["title", "brand_title", "description_description", "category_title", "services_title",
                     "variation_title", "color_title"]

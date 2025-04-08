from django.db.models.aggregates import Avg
import json
import hashlib
from django.utils.decorators import method_decorator
from rest_framework import filters, permissions
from main.models import Product, Category, Section, Image
from main.serializers import ProductSerializer, CategorySerializer, SectionSerializer, ImageSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .filters import ProductFilter
# Create your views here.

# Product

# class ProductViewSet(viewsets.ModelViewSet):
#    queryset = Product.objects.annotate(avg_rating=Avg('comments__rating')).prefetch_related('images', 'comments').select_related('section')
#    serializer_class = ProductSerializer
#    filter_backends = [filters.SearchFilter]
#    search_fields = ['name','description']
#    filter_class = ProductFilter
#
#    def get_permissions(self):
#        if self.request.user.is_superuser:
#            return [AllowAny()]
#        else:
#            return [IsAuthenticatedOrReadOnly()]

from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import filters
from django.db.models import Avg
from django.views.decorators.cache import cache_page
from functools import wraps
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly



# class ProductViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name', 'description']
#     filterset_class = ProductFilter
#     permission_classes = [AllowAny]
#
#     def get_queryset(self):
#         return Product.objects.annotate(
#             avg_rating=Avg('comments__rating')
#         ).prefetch_related('images', 'comments').select_related('section')
#
#     def _generate_cache_key(self, request):
#         query_params = request.query_params.dict()
#         key_string = json.dumps(query_params, sort_keys=True)
#         hashed = hashlib.md5(key_string.encode()).hexdigest()
#         return f"product-list:{hashed}"
#
#     def list(self, request, *args, **kwargs):
#         cache_key = self._generate_cache_key(request)
#         cached_data = cache.get(cache_key)
#
#         if cached_data:
#             return Response(cached_data)
#
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             paginated_response = self.get_paginated_response(serializer.data)
#             cache.set(cache_key, paginated_response.data, timeout=300)
#             return paginated_response
#
#         serializer = self.get_serializer(queryset, many=True)
#         data = serializer.data
#         cache.set(cache_key, data, timeout=300)
#         return Response(data)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    filter_class = ProductFilter

    def get_permissions(self):
        if self.request.user.is_superuser:
            return [AllowAny()]
        else:
            return [AllowAny()]

    def get_queryset(self):
        cache_key = 'products'
        cached_products = cache.get(cache_key)
        if cached_products:
            return cached_products
        cached_products = Product.objects.annotate(avg_rating=Avg('comments__rating')).prefetch_related('images', 'comments').select_related('section')
        cache.set(cache_key, cached_products,timeout=60*3)
        print('cache ornatildi')
        return cached_products
# Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().prefetch_related('sections')
    serializer_class = CategorySerializer

    def get_permissions(self):
      if self.request.method in permissions.SAFE_METHODS:
        return [AllowAny()]
      else:
        return [IsAuthenticated()]

    def get_queryset(self):
        cache_key = 'categories'
        cached_categories = cache.get(cache_key)
        if cached_categories:
            return cached_categories
        cached_categories = Category.objects.all().prefetch_related('sections')
        cache.set(cache_key, cached_categories,timeout=60*3)
        print('cache ornatildi')
        return cached_categories
# Section

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all().select_related('category')
    serializer_class = SectionSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    def get_queryset(self):
        cache_key = 'sections'
        cached_sections = cache.get(cache_key)
        if cached_sections:
            return cached_sections
        cached_sections = Section.objects.all().select_related('category')
        cache.set(cache_key, cached_sections,timeout=60*3)
        print('cache ornatildi')
        return cached_sections
# Image

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().select_related('product')
    serializer_class = ImageSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    def get_queryset(self):
        cache_key = 'images'
        cached_images = cache.get(cache_key)
        if cached_images:
            return cached_images
        cached_images = Image.objects.all().select_related('product')
        cache.set(cache_key, cached_images,timeout=60*3)
        print('cache ornatildi')
        return cached_images

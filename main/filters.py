import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # Ismi bo'yicha filtr
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')  # Minimum narx
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')  # Maximum narx
    category = django_filters.CharFilter(lookup_expr='icontains')  # Kategoriyaga qarab filtr

    class Meta:
        model = Product
        fields = ['name', 'price', 'category']

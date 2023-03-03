import django_filters
from .models import Todo

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    due_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Todo
        fields = {
            'id': ['exact'],
            'name': ['icontains'],
            'status': ['exact', 'iexact'],
            'priority': ['exact', 'iexact'],
            'due_date': ['gte', 'lte']
        }

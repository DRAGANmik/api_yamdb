import django_filters
from .models import Title


class TitleFilter(django_filters.FilterSet):

    genre = django_filters.CharFilter(method='genre_filter')
    category = django_filters.CharFilter(method='category_filter')
    name = django_filters.CharFilter(lookup_expr='icontains')

    def genre_filter(self, queryset, name, value):
        return queryset.filter(**{
            'genre__slug__iexact': value,
        })

    def category_filter(self, queryset, name, value):
        return queryset.filter(**{
            'category__slug__iexact': value,
        })

    class Meta:
        model = Title
        fields = [
            'genre', 'category', 'name', 'year'
        ]

import django_filters

from .models import Book


class FilterBooks(django_filters.FilterSet):
    class Meta:
        model = Book()
        fields = ['title', 'author', 'category']

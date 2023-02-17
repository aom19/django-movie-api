
from django_filters import rest_framework as filters
from .models import Movie
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MovieFilter(filters.FilterSet):
    year = filters.RangeFilter()
    genre = filters.CharFilter(field_name="genres__name", lookup_expr="in")

    class Meta:
        model = Movie
        fields = ['year', 'genre']


class PaginationMovies(PageNumberPagination):
    page_size = 1
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

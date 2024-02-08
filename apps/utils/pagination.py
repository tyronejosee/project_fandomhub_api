"""Pagination for Utils App."""

from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    """Pagination class for small sets of data."""
    page_query_param = 'p'
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 6


class MediumSetPagination(PageNumberPagination):
    """Pagination class for medium sets of data."""
    page_query_param = 'p'
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12


class LargeSetPagination(PageNumberPagination):
    """Pagination class for large sets of data."""
    page_query_param = 'p'
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 24

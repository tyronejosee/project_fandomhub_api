"""Pagination for Utils App."""

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination


class LimitSetPagination(LimitOffsetPagination):
    """Pagination class for datasets with limit and offset."""

    default_limit = 25
    limit_query_description = "Number of results to return per page."
    limit_query_param = "limit"
    max_limit = 50
    offset_query_description = "The initial index from which to return the results."
    offset_query_param = "offset"
    template = "rest_framework/pagination/numbers.html"


class SmallSetPagination(PageNumberPagination):
    """Pagination class for small sets of data."""

    page_query_param = "p"
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10


class MediumSetPagination(PageNumberPagination):
    """Pagination class for medium sets of data."""

    page_query_param = "p"
    page_size = 15
    page_size_query_param = "page_size"
    max_page_size = 15


class LargeSetPagination(PageNumberPagination):
    """Pagination class for large sets of data."""

    page_query_param = "p"
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 25

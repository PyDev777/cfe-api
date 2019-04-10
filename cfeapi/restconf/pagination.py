from rest_framework import pagination


class CFEAPIPagination(pagination.LimitOffsetPagination):  # .PageNumberPagination):
    page_size = 5

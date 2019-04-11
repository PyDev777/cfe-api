"""
status-api URL Configuration
"""

from django.conf.urls import url
from .views import (
    StatusAPIView,
    StatusDetailAPIView,
)

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusDetailAPIView.as_view(), name='detail'),
]


# Start with

# status/api/ --> List
# status/api/create/ --> Create
# status/api/1/ --> Detail
# status/api/1/update/ --> Update
# status/api/1/delete/ --> Delete

# End with

# status/api/ --> List --> CRUD
# status/api/1/ --> Detail --> CRUD

# Final

# status/api/ --> CRUD & LS

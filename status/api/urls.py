"""
status-api URL Configuration
"""

from django.conf.urls import url
# from .views import StatusListSearchAPIView
from .views import (
    StatusAPIView,
    # StatusCreateAPIView,
    StatusDetailAPIView
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
)

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    # url(r'^$', StatusListSearchAPIView.as_view()),
    # url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
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

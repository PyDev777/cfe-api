"""
status-api URL Configuration
"""

from django.conf.urls import url
# from .views import StatusListSearchAPIView
from .views import StatusAPIView

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    # url(r'^$', StatusListSearchAPIView.as_view()),
    # url(r'^create/$', StatusCreateAPIView.as_view()),
    # url(r'^(?P<id>.*)/$', StatusDetailAPIView.as_view()),
    # url(r'^(?P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
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

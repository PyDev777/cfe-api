from django.conf.urls import url

from .views import UpdateModelDetailAPIView, UpdateModelListAPIView

urlpatterns = [
    url(r'^$', UpdateModelListAPIView.as_view()),  # List, Create
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()),
]

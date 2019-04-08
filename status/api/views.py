import json
from rest_framework import generics, mixins
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.views.generic import View

from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404

from .utils import is_json


# CreateModelMixin --- POST method
# UpdateModelMixin --- PUT method
# DestroyModelMixin --- DELETE method

class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(update_by_user=self.request.user)
    #
    # def perform_destroy(self, instance):
    #     print('----')
    #     print('perform_destroy instance IS:', instance)
    #     print('----')
    #     if instance is not None:
    #         return instance.delete()
    #     return None


class StatusAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.ListAPIView):

    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    passed_id = None

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

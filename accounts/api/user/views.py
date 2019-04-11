from django.contrib.auth import get_user_model
from rest_framework import generics, pagination, permissions
from rest_framework.response import Response

from .serializers import UserDetailSerializer
from status.models import Status
from status.api.serializers import StatusInLineUserSerializer
from cfeapi.restconf.pagination import CFEAPIPagination
from status.api.views import StatusAPIView


User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):

    queryset = User.objects.filter(is_active=True)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    lookup_field = 'username'  # id

    def get_serializer_context(self):
        return {'request': self.request}


class UserStatusAPIView(StatusAPIView):

    serializer_class = StatusInLineUserSerializer
    # pagination_class = CFEAPIPagination
    # search_fields = ('user__username', 'content')

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username', None)

        if username is None:
            return Status.objects.none()

        return Status.objects.filter(user__username=username)

    def post(self, request, *args, **kwargs):
        return Response({'detail': 'Not Allowed!'}, status=400)

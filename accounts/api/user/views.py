from django.contrib.auth import get_user_model
from rest_framework import generics, pagination, permissions

from .serializers import UserDetailSerializer
from status.models import Status
from status.api.serializers import StatusInLineUserSerializer
from cfeapi.restconf.pagination import CFEAPIPagination


User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):

    queryset = User.objects.filter(is_active=True)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    lookup_field = 'username'  # id

    def get_serializer_context(self):
        return {'request': self.request}


class UserStatusAPIView(generics.ListAPIView):

    serializer_class = StatusInLineUserSerializer
    pagination_class = CFEAPIPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username', None)

        if username is None:
            return Status.objects.none()

        return Status.objects.filter(user__username=username)

import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework import serializers
from status.api.serializers import StatusInLineUserSerializer
from status.models import Status


User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):

    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status',
        ]

    def get_uri(self, obj):
        return "/api/users/{id}/".format(id=obj.id)

    def get_status(self, obj):
        request = self.context.get('request', None)
        limit = 10
        if request:
            limit_query = request.GET.get('limit', None)

            try:
                limit = int(limit_query)
            except:
                pass

        qs = Status.objects.filter(user=obj).order_by('-created_at')
        data = {
            'uri': self.get_uri(obj) + 'status/',
            'last': StatusInLineUserSerializer(qs.last()).data,
            'recent': StatusInLineUserSerializer(qs[:limit], many=True).data,
        }
        return data

    # def get_recent_status(self, obj):
    #     return StatusInLineUserSerializer(qs, many=True).data

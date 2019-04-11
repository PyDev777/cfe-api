from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from status.models import Status
from accounts.api.serializers import UserPublicSerializer


class StatusSerializer(serializers.ModelSerializer):

    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    # user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']

    def get_uri(self, obj):
        request = self.context.get('request', None)
        # return "/api/status/{id}/".format(id=obj.id)
        return api_reverse('api-status:detail', kwargs={'id': obj.id}, request=request)

    # def get_user(self, obj):
    #     request = self.context.get('request', None)
    #     user = obj.user
    #     return UserPublicSerializer(user, read_only=True, context={'request': request}).data

    def validate_content(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('StatusSerializer: Content is too long!')
        return value

    def validate(self, data):
        content = data.get('content', None)
        if content == '':
            content = None

        image = data.get('image', None)
        if image == '':
            image = None

        if content is None and image is None:
            raise serializers.ValidationError('StatusSerializer: Content or Image is required!')

        return data


class StatusInLineUserSerializer(StatusSerializer):

    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'content',
            'image',
        ]


# ----------------------------------------------------------------------------------------------------

# class StatusInLineUserSerializer(serializers.ModelSerializer):
#
#     uri = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Status
#         fields = [
#             'uri',
#             'id',
#             'content',
#             'image',
#         ]
#
#     def get_uri(self, obj):
#         request = self.context.get('request', None)
#         # return "/api/status/{id}/".format(id=obj.id)
#         return api_reverse('api-status:detail', kwargs={'id': obj.id}, request=request)
#
#     def validate_content(self, value):
#         if len(value) > 100:
#             raise serializers.ValidationError('StatusSerializer: Content is too long!')
#         return value
#
#     def validate(self, data):
#         content = data.get('content', None)
#         if content == '':
#             content = None
#
#         image = data.get('image', None)
#         if image == '':
#             image = None
#
#         if content is None and image is None:
#             raise serializers.ValidationError('StatusSerializer: Content or Image is required!')
#
#         return data


# class CustomSerializer(serializers.Serializer):
#
#     content = serializers.CharField()
#     email = serializers.EmailField()

from rest_framework import serializers
from status.models import Status

from accounts.api.serializers import UserPublicSerializer


class CustomSerializer(serializers.Serializer):

    content = serializers.CharField()
    email = serializers.EmailField()


class StatusSerializer(serializers.ModelSerializer):

    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Status
        fields = ['id', 'user', 'content', 'image', 'uri']
        read_only_fields = ['user']

    def get_uri(self, obj):
        return "/api/status/{id}/".format(id=obj.id)

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

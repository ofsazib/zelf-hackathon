from rest_framework import serializers
from core.models import (
    Content
)

class ContentWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = (
            'id',
            'content',
            'creator',
        )


class ContentBulkWriteSerializer(serializers.Serializer):
    data = ContentWriteSerializer(many=True)

    def create(self, validated_data):
        print(validated_data)
        return None

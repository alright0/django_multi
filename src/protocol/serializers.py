from rest_framework import serializers
from protocol.models import Screen

class ImageScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ('image', 'description')

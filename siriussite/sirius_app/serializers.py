from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    """
    Image Serializer
    """
    class Meta:
        model = Image
        fields = ('picture', 'description')
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Image
from .serializers import ImageSerializer


# ------------API----------------
class ImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet для просмотра и редактирования изображений
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer



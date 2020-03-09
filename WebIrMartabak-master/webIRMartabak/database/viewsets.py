from rest_framework import viewsets
from .models import martabakhome
from .serializer import MartabakhomeSerializer
class martabakhomeViewSet(viewsets.ModelViewSet):
    queryset = martabakhome.objects.all()
    serializer_class = MartabakhomeSerializer
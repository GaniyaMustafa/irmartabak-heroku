from rest_framework import serializers
from .models import martabakhome

class MartabakhomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = martabakhome
        fields = '__all__'
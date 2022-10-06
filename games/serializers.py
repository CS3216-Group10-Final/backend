from platform import platform
from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    cover = serializers.CharField(source='cover.url')
    class Meta:
        model = Game
        fields = '__all__'#['id', 'name', 'cover', 'genres', 'platforms', 'franchise']
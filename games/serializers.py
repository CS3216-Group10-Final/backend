from platform import platform
from typing import Dict
from rest_framework import serializers
from .models import Game, GameEntry, Genre, Platform

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'#['id', 'name', 'cover', 'genres', 'platforms', 'franchise']


class GameEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameEntry
        fields = '__all__'




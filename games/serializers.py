from platform import platform
from typing import Dict
from rest_framework import serializers
from .models import Game, GameEntry, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    #genres = GenreSerializer(many=True)

    class Meta:
        model = Game
        fields = '__all__'#['id', 'name', 'cover', 'genres', 'platforms', 'franchise']

    '''
    def validate_cover(self, value):
        if type(value) == type({}) and 'url' in value.keys():
            return value['url']
        raise serializers.ValidationError("Invalid format: cover")
    '''  

class GameEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameEntry
        fields = '__all__'




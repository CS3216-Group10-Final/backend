from dataclasses import fields
from rest_framework import serializers
from .models import Activity
from users.models import User
from games.models import Game, GameEntry
from users.serializers import UserSerializer
from games.serializers import GameSerializer

class ActivitySerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'


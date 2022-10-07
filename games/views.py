from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from igdb.wrapper import IGDBWrapper
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from games.serializers import GameSerializer
from .models import Game

from displaycase import igdbapi_pb2
import requests
import os

# Create your views here.

class GamesView(APIView):

    def get(self, request):
        search_query = request.query_params.get('query')
        paginator = PageNumberPagination()

        games = Game.objects.all()

        if search_query:
            games = games.filter(name__icontains=search_query)
        
        queryset = paginator.paginate_queryset(games, request)
        serializer = GameSerializer(queryset, many=True)
        response = Response(serializer.data)
        return response

class GameView(APIView):
    
    def get(self, request, id):
        try:
            game = Game.objects.get(id__iexact=id)
            serializer = GameSerializer(game)
            response = Response(serializer.data)
        except:
            response = Response("Game not found.", status=status.HTTP_404_NOT_FOUND)
        return response
        
        
class GameEntriesView(APIView):

    def get(self, request):
        search_query = request.query_params.get('query')
        user_id = request.query_params.get('user_id')
        game_id = request.query_params.get('game_id')


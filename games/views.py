from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from igdb.wrapper import IGDBWrapper
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from games.serializers import GameSerializer, GameEntrySerializer
from .models import Game, GameEntry

from displaycase import igdbapi_pb2
import requests
import os


class GamesView(APIView):
    
    def get(self, request):
        search_query = request.query_params.get('query')
        paginator = PageNumberPagination()

        games = Game.objects.all().order_by('name')

        if search_query:
            games = games.filter(name__icontains=search_query)
        
        queryset = paginator.paginate_queryset(games, request)
        serializer = GameSerializer(queryset, many=True)
        response = Response(serializer.data)
        response.headers = {'Pages': str(paginator.page.paginator.num_pages)}
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
        paginator = PageNumberPagination()

        entries = GameEntry.objects.all().order_by('id')

        if search_query:
            entries = entries.filter(game__name__icontains=search_query)

        if user_id:
            entries = entries.filter(user__id=user_id)

        if game_id:
            entries = entries.filter(game__id=game_id)

        queryset = paginator.paginate_queryset(entries, request)
        serializer = GameEntrySerializer(queryset, many=True)
        response = Response(serializer.data)
        response.headers = {'Pages': str(paginator.page.paginator.num_pages)}
        return response
        
    def post(self, request):
        data = request.data
        serializer = GameEntrySerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.save().__str__())
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameEntryView(APIView):

    def get(self, request, id):
        try:
            game = GameEntry.objects.get(id__iexact=id)
            serializer = GameEntrySerializer(game)
            response = Response(serializer.data)
        except:
            response = Response("Game entry not found.", status=status.HTTP_404_NOT_FOUND)
        return response

    def put(self, request, id):
        try:
            game = GameEntry.objects.get(id__iexact=id)
            serializer = GameEntrySerializer(game, data=request.data)
            if serializer.is_valid():
                response = Response(serializer.save().__str__())
            else:
                response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            response = Response("Game entry not found.", status=status.HTTP_404_NOT_FOUND)
        return response

    def delete(self, request, id):
        try:
            game = GameEntry.objects.get(id__iexact=id)
            game.delete()
            response = Response(game.__str__())
        except:
            response = Response("Game entry not found.", status=status.HTTP_404_NOT_FOUND)
        return response

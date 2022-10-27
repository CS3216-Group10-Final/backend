from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from games.serializers import GameSerializer, GameEntrySerializer, ReviewSerializer
from .models import Game, GameEntry
from activities.models import Activity
from follows.models import Follow

import requests
import os


class GamesView(APIView):
    
    def get(self, request):
        search_query = request.query_params.get('query')
        paginator = PageNumberPagination()
        paginator.page_size = 20

        games = Game.objects.all().order_by('-rating_count', '-first_release_date')

        if search_query:
            games = games.filter(Q(name__icontains=search_query) | Q(alternative_names__icontains=search_query))
        
        queryset = paginator.paginate_queryset(games, request)
        serializer = GameSerializer(queryset, many=True)
        response = Response(serializer.data)
        response.headers = {
            'Pages': str(paginator.page.paginator.num_pages),
            'Access-Control-Expose-Headers': '*'}
        return response

class GameView(APIView):
    
    def get(self, request, id):
        try:
            game = Game.objects.get(id__iexact=id)
            serializer = GameSerializer(game)
            response = Response(serializer.data)
        except Game.DoesNotExist:
            response = Response("Game not found.", status=status.HTTP_404_NOT_FOUND)
        return response
        
        
class GameEntriesView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
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
        response.headers = {
            'Pages': str(paginator.page.paginator.num_pages),
            'Access-Control-Expose-Headers': '*'}
        return response
        
    def post(self, request):
        data = request.data
        serializer = GameEntrySerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        queryset = GameEntry.objects.filter(game__id=data['game_id'], user=request.user)
        if len(queryset) > 0:
            return Response("GameEntry already exists.", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        new_game = serializer.save()
        Activity.generateActivities(new_game, request.user, original_status=None, original_rating=None, original_review='')
        return Response(serializer.data)


class GameEntryView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        try:
            game = GameEntry.objects.get(id__iexact=id)
            serializer = GameEntrySerializer(game)
            response = Response(serializer.data)
        except GameEntry.DoesNotExist:
            response = Response("Game entry not found.", status=status.HTTP_404_NOT_FOUND)
        return response

    def put(self, request, id):
        try:
            game = GameEntry.objects.get(id__iexact=id)

            original_status = game.status
            original_rating = game.rating
            original_review = game.review

            if game.user != request.user:
                return Response("Cannot edit other user game entries.", status=status.HTTP_401_UNAUTHORIZED)

            if request.data['user_id'] != request.user.id:
                return Response("Cannot edit user_id field.", status=status.HTTP_401_UNAUTHORIZED)

            serializer = GameEntrySerializer(game, data=request.data)
            if serializer.is_valid():
                new_game = serializer.save()
                Activity.generateActivities(new_game, request.user, original_status, original_rating, original_review)
                response = Response(serializer.data)
            else:
                response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except GameEntry.DoesNotExist:
            response = Response("Game entry not found.", status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
        return response

    def delete(self, request, id):
        try:
            game = GameEntry.objects.get(id__iexact=id)
            serializer = GameEntrySerializer(game)
            response = Response(serializer.data)
            game.delete()
        except GameEntry.DoesNotExist:
            response = Response("Game entry not found.", status=status.HTTP_404_NOT_FOUND)
        return response

class ReviewsView(APIView):
    
    def get(self, request):
        queryset = GameEntry.objects.all()
        
        game_id = request.query_params.get('game_id')
        following_only = request.query_params.get('following_only')
        if game_id:
            queryset = queryset.filter(game__id=game_id)
        if following_only and following_only.lower() == "true" and request.user.is_authenticated:
            followees = Follow.get_followees_of(request.user)
            queryset = queryset.filter(user__in=followees)

        paginator = PageNumberPagination()
        paginator.page_size = 20
        queryset = paginator.paginate_queryset(queryset, request)

        serializer = ReviewSerializer(queryset, many=True)
        response = Response(serializer.data)
        response.headers = {
            'Pages': str(paginator.page.paginator.num_pages),
            'Access-Control-Expose-Headers': '*'}
        return response
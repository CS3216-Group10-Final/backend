from re import A
from datetime import datetime, timedelta
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from games.serializers import GameSerializer, GameEntrySerializer, ReviewSerializer
from .models import Game, GameEntry, Platform, Genre
from activities.models import Activity
from follows.models import Follow

import requests
import os


class GamesView(APIView):
    
    def get(self, request):
        search_query = request.query_params.get('query')
        release_years = request.GET.getlist('release_year')
        genres = request.GET.getlist('genre')
        platforms = request.GET.getlist('platform')


        paginator = PageNumberPagination()
        paginator.page_size = 20

        games = Game.objects.all().order_by('-rating_count', '-first_release_date')

        if search_query:
            games = games.filter(Q(name__icontains=search_query) | Q(alternative_names__icontains=search_query))

        if release_years:
            year_list = []
            for year in release_years:
                if year.isdigit():
                    year_list.append(year)
            if year_list:
                games = games.filter(first_release_date__year__in=year_list)

        if genres:
            genre_list = []
            for genre in genres:
                genre = Genre.objects.filter(name__icontains=genre).first()
                if genre:
                    genre_list.append(genre)
            if genre_list:
                games = games.filter(genres__in=genre_list).distinct()

        if platforms:
            platform_list = []
            for platform in platforms:
                platform = Platform.objects.filter(name__icontains=platform).first()
                if platform:
                    platform_list.append(platform)
            if platform_list:
                games = games.filter(platforms__in=platform_list).distinct()
        
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

class PopularNowGamesView(APIView):

    def get(self, request):
        DAY_RANGE = 182 
        date_now = datetime.today()
        date_start = date_now + timedelta(days=-DAY_RANGE)

        games = Game.objects.filter(first_release_date__gte=date_start).order_by('-rating_count', '-first_release_date')[:20]

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
        



        
class GameEntriesView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        search_query = request.query_params.get('query')
        user_id = request.query_params.get('user_id')
        game_id = request.query_params.get('game_id')
        release_years = request.GET.getlist('release_year')
        genres = request.GET.getlist('genre')
        platforms = request.GET.getlist('platform')
        paginator = PageNumberPagination()

        entries = GameEntry.objects.all().order_by('id')

        if search_query:
            entries = entries.filter(game__name__icontains=search_query)

        if user_id:
            entries = entries.filter(user__id=user_id)

        if game_id:
            entries = entries.filter(game__id=game_id)

        if release_years:
            year_list = []
            for year in release_years:
                if year.isdigit():
                    year_list.append(year)
            if year_list:
                entries = entries.filter(game__first_release_date__year__in=year_list)

        if genres:
            genre_list = []
            for genre in genres:
                genre = Genre.objects.filter(name__icontains=genre).first()
                if genre:
                    genre_list.append(genre)
            if genre_list:
                entries = entries.filter(game__genres__in=genre_list).distinct()

        if platforms:
            platform_list = []
            for platform in platforms:
                platform = Platform.objects.filter(name__icontains=platform).first()
                if platform:
                    platform_list.append(platform)
            if platform_list:
                entries = entries.filter(platforms__in=platform_list).distinct()

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
        has_rating = request.query_params.get('has_rating')
        has_review = request.query_params.get('has_review')
        if game_id:
            queryset = queryset.filter(game__id=game_id)
        if following_only and following_only.lower() == "true" and request.user.is_authenticated:
            followees = Follow.get_followees_of(request.user)
            queryset = queryset.filter(user__in=followees)
        if has_rating and has_rating.lower() == "true":
            queryset = queryset.exclude(rating__isnull=True)
        if has_review and has_review.lower() == "true":
            queryset = queryset.exclude(review__isnull=True).exclude(review__exact='')

        paginator = PageNumberPagination()
        paginator.page_size = 20
        queryset = paginator.paginate_queryset(queryset, request)

        serializer = ReviewSerializer(queryset, many=True)
        response = Response(serializer.data)
        response.headers = {
            'Pages': str(paginator.page.paginator.num_pages),
            'Access-Control-Expose-Headers': '*'}
        return response

class ImportSteamGames(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        steamid = user.steamid
        if not steamid:
            return Response('Steam account not linked', status=status.HTTP_405_METHOD_NOT_ALLOWED)

        url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={os.getenv("STEAM_API_KEY")}&steamid={steamid}&format=json&include_appinfo=True&include_played_free_games=True'
        r = requests.get(url)
        try:
            data = r.json()
            data = data['response']
        except:
            return Response(r.content, status=status.HTTP_400_BAD_REQUEST)

        try:
            if 'games' not in data or 'game_count' not in data:
                return Response(
                    {
                        'error_code': 1,
                        'error_message': "No games found. Make sure your Steam 'Game details' privacy setting is set to public."
                    })

            count = data['game_count']
            games = data['games']

            #match by name and alternative_names? or by website(steamappid in igdb database) 
            #consider parent_game and version_parent
            appids = []
            for game in games:
                appid = game['appid']
                appids.append(appid)
            
            
            displaycasegameentries = GameEntry.objects.filter(user=user).values_list('game', flat=True)
            displaycasegameentries = list(displaycasegameentries)
            displaycasegames = Game.objects.filter(id__in=displaycasegameentries)
            steamgames = Game.objects.filter(steamappid__in=appids)

            remaining = steamgames.difference(displaycasegames)

            paginator = PageNumberPagination()
            queryset = paginator.paginate_queryset(remaining, request)

            serializer = GameSerializer(queryset, many=True)
            response = Response(serializer.data)
            response.headers = {
                'Pages': str(paginator.page.paginator.num_pages),
                'Access-Control-Expose-Headers': '*'}
            return response


        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        game_status = request.query_params.get('status')
        if game_status is not None and game_status.isdigit():
            game_status = int(game_status)
            if game_status not in GameEntry.GameEntryStatus.values:
                game_status = GameEntry.GameEntryStatus.COMPLETED.value
        else:
            game_status = GameEntry.GameEntryStatus.COMPLETED.value 
        steamid = request.user.steamid
        if not steamid:
            return Response('Steam account not linked', status=status.HTTP_405_METHOD_NOT_ALLOWED)

        url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={os.getenv("STEAM_API_KEY")}&steamid={steamid}&format=json&include_appinfo=True&include_played_free_games=True'
        r = requests.get(url)
        data = r.json()
        data = data['response']

        try:
            count = data['game_count']
            games = data['games']

            #match by name and alternative_names? or by website(steamappid in igdb database) 
            #consider parent_game and version_parent
            appids = []
            for g in games:
                appid = g['appid']
                appids.append(appid)
            
            
            displaycasegameentries = GameEntry.objects.filter(user=request.user).values_list('game', flat=True)
            displaycasegameentries = list(displaycasegameentries)
            displaycasegames = Game.objects.filter(id__in=displaycasegameentries)
            steamgames = Game.objects.filter(steamappid__in=appids)

            remaining = steamgames.difference(displaycasegames)
            pc = Platform.objects.get(name__icontains='PC (MICROSOFT WINDOWS)')

            entries = []
            for g in remaining:
                entry = GameEntry(user=request.user, game=g, status=game_status)
                entry.save()
                entries.append(entry)

            paginator = PageNumberPagination()
            queryset = paginator.paginate_queryset(entries, request)

            serializer = GameEntrySerializer(queryset, many=True)
            response = Response(serializer.data)
            response.headers = {
                'Pages': str(paginator.page.paginator.num_pages),
                'Access-Control-Expose-Headers': '*'}
            return response


        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

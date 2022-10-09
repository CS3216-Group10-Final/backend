from datetime import datetime
import time
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from igdb.wrapper import IGDBWrapper
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from games.serializers import GameSerializer, GenreSerializer, PlatformSerializer
from .models import Game, Genre, Platform

from displaycase import igdbapi_pb2
import requests
import os

def updateToken():
    client_id = os.getenv("DISPLAYCASE_CLIENT_ID", "")
    client_secret = os.getenv("DISPLAYCASE_CLIENT_SECRET", "")
    url = "https://id.twitch.tv/oauth2/token?grant_type=client_credentials&client_id=" 
    url += client_id + "&client_secret=" + client_secret
    r = requests.post(url)
    try:
        data = r.json()
        token = data["access_token"]
        os.environ["TWITCH_AUTH"] = token
        return token
    except:
        raise Exception("Error obtaining access token."    )
    
def updateGames():
    token = os.getenv("TWITCH_AUTH")
    client_id = os.getenv("DISPLAYCASE_CLIENT_ID", "")

    if token is None:
        token = updateToken()
        
    url = "https://api.igdb.com/v4/games"
    headers = {"Client-ID": client_id, "Authorization": "Bearer " + token}
    offset = 0
    while offset < 208000:
        query = 'fields name, cover.url, genres.name, platforms.name, first_release_date, summary, franchise.name; limit 500; offset '
        query += str(offset) + ';'
        r = requests.post(url, data=query, headers=headers)
        data = r.json()
        for game in data:
            
            if 'cover' in game:
                cover_url = game['cover']['url']
                game['cover'] = 'https:' + cover_url.replace('t_thumb', 't_1080p')
            if 'genres' in game:
                game['genres'] = list(map(lambda a : a['name'], game['genres']))
            if 'platforms' in game:
                game['platforms'] = list(map(lambda a : a['name'], game['platforms']))
            if 'first_release_date' in game:
                game['first_release_date'] = datetime.utcfromtimestamp(game['first_release_date']).isoformat()
            if 'franchise' in game:
                game['franchise'] = game['franchise']['name']
            serializer = GameSerializer(data=game)
            #print(game)
            if not serializer.is_valid():
                print(serializer.errors)
            serializer.save()
        print(offset)
        offset += 500
    

def updateGenres():
    token = os.getenv("TWITCH_AUTH")
    client_id = os.getenv("DISPLAYCASE_CLIENT_ID", "")

    if token is None:
        token = updateToken()
        
    url = "https://api.igdb.com/v4/genres"
    headers = {"Client-ID": client_id, "Authorization": "Bearer " + token}
    r = requests.post(url, data='fields name; limit 500;', headers=headers)
    data = r.json()
    serializer = GenreSerializer(data=data, many=True)
    print(serializer.is_valid())
    print(serializer.errors)
    print(serializer.save())
    serializer = GenreSerializer(Genre.objects.all(), many=True)
    print(serializer.data)

def updatePlatforms():
    token = os.getenv("TWITCH_AUTH")
    client_id = os.getenv("DISPLAYCASE_CLIENT_ID", "")

    if token is None:
        token = updateToken()
        
    url = "https://api.igdb.com/v4/platforms"
    headers = {"Client-ID": client_id, "Authorization": "Bearer " + token}
    r = requests.post(url, data='fields name; limit 500;', headers=headers)
    data = r.json()
    serializer = PlatformSerializer(data=data, many=True)
    print(serializer.is_valid())
    print(serializer.errors)
    print(serializer.save())
    serializer = PlatformSerializer(Platform.objects.all(), many=True)
    print(serializer.data)
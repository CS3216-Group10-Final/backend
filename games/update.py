from datetime import datetime
import time
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from games.serializers import GameSerializer, GenreSerializer, PlatformSerializer
from .models import Game, Genre, Platform

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

def updateAllGames():
    updateGames(0, 210000)

def updateGames(start, end):
    token = os.getenv("TWITCH_AUTH")
    client_id = os.getenv("DISPLAYCASE_CLIENT_ID", "")

    if token is None:
        token = updateToken()
        
    url = "https://api.igdb.com/v4/games"
    headers = {"Client-ID": client_id, "Authorization": "Bearer " + token, "Content-Type": "application/json"}
    offset = start
    while offset < end:
        query = 'fields name, cover.url, genres.name, platforms.name, first_release_date, summary, franchise.name, involved_companies.*, alternative_names.name, rating_count, websites.*; limit 500; offset '
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
            if 'alternative_names' in game:
                names = map(lambda a : a['name'], game['alternative_names'])
                game['alternative_names'] = ', '.join(names)
            if 'websites' in game:
                for w in game['websites']:
                    if 'category' in w and w['category'] == 13:
                        steamurl = w['url']
                        post = steamurl.split('app/')[-1]
                        steamappid = post.split('/')[0]
                        game['steamappid'] = steamappid
            #if 'involved_companies' in game:
                #for company in game['involved_companies']:
                    #if company['publisher']:
                    #if company['developer']:
            try:
                obj = Game.objects.get(id=game['id'])
                serializer = GameSerializer(obj, data=game)
            except:
                serializer = GameSerializer(data=game)
            if not serializer.is_valid():
                print(serializer.errors)
            else:
                serializer.save()
        print(offset + 500)
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
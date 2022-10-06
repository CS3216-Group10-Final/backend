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
    r = requests.post(url, data='fields name, cover.url; where id=(22,33);', headers=headers)
    data = r.json()
    print(data)
    serializer = GameSerializer(data=data, many=True)
    serializer.is_valid()
    serializer.save()
    print(Game.objects.all())


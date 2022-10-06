from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from igdb.wrapper import IGDBWrapper
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Game

from displaycase import igdbapi_pb2
import requests
import os

# Create your views here.

class UpdateGamesTest(APIView):
    def updateToken(self):
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
            raise Exception("Error obtaining access token.")
    
    def post(self, request):
        token = os.getenv("TWITCH_AUTH")
        client_id = os.getenv("DISPLAYCASE_CLIENT_ID", "")

        if token is None:
            token = self.updateToken()
        
        url = "https://api.igdb.com/v4/games"
        headers = {"Client-ID": client_id, "Authorization": "Bearer " + token}
        r = requests.post(url, data='fields name; where id=(22,33);', headers=headers)
        data = r.json()
        print(data)
        #deserialize to model
        # loop through all games
        # run on shell instead of view due to rate limits
        '''
        data = r.content
        gameResult = igdbapi_pb2.GameResult()
        print(data)
        gameResult.ParseFromString(data)
        print(gameResult)
        for game in gameResult.games:
            print(type(game))
            print(game.name)
        game = Game()
        game.from_pb(data)
        print(game)
        '''
        
        
        
        
            



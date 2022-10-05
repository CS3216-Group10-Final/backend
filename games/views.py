from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

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

        if token is None:
            token = self.updateToken()
        
        
        
        
        
            



from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from .models import Follow

class FollowActionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        try:
            followee = User.objects.get(username=username)
        except User.DoesNotExist:
            response = Response("There is no user with the given username.", status=status.HTTP_400_BAD_REQUEST)
            return response
        
        follower = request.user

        follow = Follow.objects.get_or_create(followee=followee, follower=follower)

        return Response()
    
    def delete(self, request, username):
        try:
            followee = User.objects.get(username=username)
        except User.DoesNotExist:
            response = Response("There is no user with the given username.", status=status.HTTP_400_BAD_REQUEST)
            return response
        
        follower = request.user
        
        Follow.objects.filter(followee=followee, follower=follower).delete()
        return Response()
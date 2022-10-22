from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from users.models import User
from users.serializers import UserSerializer
from .models import Follow

class FollowActionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            response = Response("There is no user with the given username.", status=status.HTTP_400_BAD_REQUEST)
            return response
        
        followers = request.query_params.get('followers')



        if followers:
            users = Follow.objects.filter(followee=request.user).values_list('follower', flat=True)
        else:
            users = Follow.objects.filter(follower=request.user).values_list('followee', flat=True)

        users = User.objects.filter(id__in=users)
        paginator = PageNumberPagination()

        queryset = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(queryset, many=True, context={'request_user': request.user})
        response = Response(serializer.data)
        response.headers = {
            'Pages': str(paginator.page.paginator.num_pages),
            'Access-Control-Expose-Headers': '*'}
        return Response(serializer.data)

    def post(self, request, username):
        try:
            followee = User.objects.get(username=username)
        except User.DoesNotExist:
            response = Response("There is no user with the given username.", status=status.HTTP_400_BAD_REQUEST)
            return response
        
        follower = request.user

        if follower == followee:
            return Response("Cannot follow yourself", status=status.HTTP_401_UNAUTHORIZED)

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
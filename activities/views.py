from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Activity
from .serializers import ActivitySerializer

from follows.models import Follow
from users.models import User

class ActivityView(APIView):

    def get(self, request, id):
        paginator = PageNumberPagination()

        entries = Activity.objects.filter(user__id=id).order_by('-time_created')

        queryset = paginator.paginate_queryset(entries, request)
        serializer = ActivitySerializer(queryset, many=True)
        response = Response(serializer.data)
        response.headers = {
            'Pages': str(paginator.page.paginator.num_pages),
            'Access-Control-Expose-Headers': '*'}
        return response

class TimelineView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        paginator = PageNumberPagination()
        search_query = request.query_params.get('query')
        username = request.query_params.get('username')
        game_id = request.query_params.get('game_id')

        # get all follows
        follows = Follow.objects.filter(follower=request.user).values_list('followee', flat=True)
        follows = list(follows)
        follows.append(request.user.id)


        #filter all activities by users in follows
        entries = Activity.objects.filter(user__id__in=follows).order_by('-time_created')
        
        if game_id:
            entries = entries.filter(game__id=game_id)

        if username:
            entries = entries.filter(user__username__icontains=username)

        if search_query:
            entries = entries.filter(Q(game__name__icontains=search_query) | Q(user__username__icontains=search_query))

        
        queryset = paginator.paginate_queryset(entries, request)
        serializer = ActivitySerializer(queryset, many=True)
        response = Response(serializer.data)
        response.headers = {
            'Pages': str(paginator.page.paginator.num_pages),
            'Access-Control-Expose-Headers': '*'}
        return response

        
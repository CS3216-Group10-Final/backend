from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Activity
from .serializers import ActivitySerializer


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

from django.urls import re_path
from rest_framework_simplejwt import views 
from activities import views

urlpatterns = [
    re_path(r'activities/(?P<id>\d+)/?$', views.ActivityView.as_view(), name='get-user-activities'),
    re_path(r'timeline/?$', views.TimelineView.as_view(), name='get-user-timeline'),
    re_path(r'timeline/recentgames/?$', views.RecentGamesView.as_view(), name='get-recent-timeline-games'),
]
from django.urls import re_path
from rest_framework_simplejwt import views 
from games import views

urlpatterns = [
    re_path(r'games/?$', views.GamesView.as_view(), name='get-games'),
    re_path(r'games/(?P<id>\d+)/?$', views.GameView.as_view(), name='get-game'),
    re_path(r'game-entries/?$', views.GameEntriesView.as_view(), name='game-entries'),
    re_path(r'game-entries/(?P<id>\d+)/?$', views.GameEntryView.as_view(), name='game-entry'),
    re_path(r'reviews/?$', views.ReviewsView.as_view(), name='reviews'),
]
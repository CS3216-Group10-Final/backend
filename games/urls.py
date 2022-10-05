from django.urls import re_path
from rest_framework_simplejwt import views 
from games import views

urlpatterns = [
    re_path(r'games/update/?$', views.UpdateGamesTest.as_view(), name='get-games'),
]
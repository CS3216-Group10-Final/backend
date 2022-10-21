from django.urls import re_path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    re_path(r'follows/(?P<username>\w+)/?$', views.FollowActionsView.as_view(), name='follow-actions'),
]
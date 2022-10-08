from django.urls import re_path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    re_path('register/?$', views.RegisterView.as_view(), name='register'),
    re_path('login/?$', views.LoginView.as_view(), name='login'),
    re_path('logout/?$', jwt_views.TokenBlacklistView.as_view(), name='logout'),
    re_path('tokens/refresh/?$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path('tokens/verify/?$', views.TokenVerifyView.as_view(), name='token_verify'),
    re_path(r'users/?$', views.UserListView.as_view(), name='user-list'),
]
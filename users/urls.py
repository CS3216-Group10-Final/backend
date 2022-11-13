from django.urls import re_path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    re_path('register/?$', views.RegisterView.as_view(), name='register'),
    re_path('login/?$', views.LoginView.as_view(), name='login'),
    re_path('login/google/?$', views.GoogleLoginView.as_view(), name='google-login'),
    re_path('login/google/callback/?$', views.GoogleLoginCallbackView.as_view(), name='google-login-callback'),
    re_path('logout/?$', jwt_views.TokenBlacklistView.as_view(), name='logout'),
    re_path('tokens/refresh/?$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path('tokens/verify/?$', views.TokenVerifyView.as_view(), name='token_verify'),
    re_path('change-password/?$', views.ChangePasswordView.as_view(), name='change-password'),
    re_path(r'users/?$', views.UserListView.as_view(), name='user-list'),
    re_path(r'users/(?P<username>\w+)/?$', views.UserDetailView.as_view(), name='user-detail'),
    re_path(r'user/?$', views.SelfUserDetailView.as_view(), name='self-user-detail'),
    re_path(r'users/(?P<username>\w+)/stats/?$', views.UserStatsView.as_view(), name='user-stats'),
]
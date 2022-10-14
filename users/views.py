from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework import generics, status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import UntypedToken
from urllib.parse import urlencode

from .models import User
from .serializers import GoogleLoginSerializer, RegisterSerializer, UserSerializer, UserStatsSerializer
from .utils import get_google_access_token, get_google_email, get_tokens_for_user

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        username = request.data.get('username')
        username_is_used = User.objects.filter(username=username).exists()
        email_is_used = User.objects.filter(email=email).exists()

        if username_is_used:
            response = Response({
                'error_code': 1,
                'error_message': 'Username is already in use.'
            })
            return response
        elif email_is_used:
            response = Response({
                'error_code': 2,
                'error_message': 'Email is already in use.'
            })
            return response

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response()

class LoginView(jwt_views.TokenObtainPairView):
    """Takes a set of user credentials. 
    If the credentials are valid, 
    returns an access and refresh JSON web token pair."""

    serializer_class = jwt_serializers.TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(request, email=email, password=password)

        if not user:
            response = Response({
                'error_code': 1,
                'error_message': 'Email and/or password is incorrect.'
            })
            return response

        response = super().post(request, *args, **kwargs)
        return response

class GoogleLoginView(APIView):
    def get(self, request, *args, **kwargs):
        domain = settings.BASE_BACKEND_URL
        path = reverse('google-login-callback')
        redirect_uri = f'{domain}{path}'
        endpoint = 'https://accounts.google.com/o/oauth2/v2/auth'
        params = urlencode({
            'response_type': 'code',
            'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
            'redirect_uri': redirect_uri,
            'prompt': 'select_account',
            'access_type': 'offline',
            'scope': 'email',
        })
        url = f'{endpoint}?{params}'
        return Response({'url': url})

class GoogleLoginCallbackView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = GoogleLoginSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        code = validated_data.get('code')
        error = validated_data.get('error')

        login_feedback_url = f'{settings.BASE_FRONTEND_URL}/login/feedback'
        response = redirect(login_feedback_url)

        if error or not code:
            params = urlencode({
                'error_code': 1,
                'error_message': 'Failed to login with Google.',
                'error_message_from_google': error
            })
            return redirect(f'{login_feedback_url}?{params}')

        domain = settings.BASE_BACKEND_URL
        path = reverse('google-login-callback')
        redirect_uri = f'{domain}{path}'

        access_token = get_google_access_token(code=code, redirect_uri=redirect_uri)
        email = get_google_email(access_token=access_token)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            email_username = email.split('@')[0]
            username = User.objects.generate_unique_username_from(email_username)
            user = User.objects.create_user(username, email, User.objects.make_random_password())

        tokens = get_tokens_for_user(user=user)
        params = urlencode(tokens)
        return redirect(f'{login_feedback_url}?{params}')

class TokenVerifyView(jwt_views.TokenVerifyView):
    serializer_class = jwt_serializers.TokenVerifySerializer

    def post(self, request, *args, **kwargs):
        token = UntypedToken(request.data.get('token'))

        jti = token.get("jti")
        if BlacklistedToken.objects.filter(token__jti=jti).exists():
            raise InvalidToken("Token is blacklisted")
        
        response = super().post(request, *args, **kwargs)
        return response

class UserListView(APIView):

    def get(self, request):
        search_query = request.query_params.get('query')
        paginator = PageNumberPagination()

        users = User.objects.all().order_by('username')

        if search_query:
            users = users.filter(username__icontains=search_query)
        
        queryset = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(queryset, many=True)
        response = Response(serializer.data)
        response.headers = {
            'Pages': str(paginator.page.paginator.num_pages),
            'Access-Control-Expose-Headers': '*'}
        return response

class UserDetailView(APIView):
    
    def get(self, request, username):
        try:
            user = User.objects.get(username__iexact=username)
        except:
            response = Response("User not found.", status=status.HTTP_404_NOT_FOUND)
            return response
        
        serializer = UserSerializer(user)
        response = Response(serializer.data)
        return response

class SelfUserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        response = Response(serializer.data)
        return response

    def patch(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        
        username = serializer.initial_data['username']
        user_with_input_username = User.objects.filter(username=username)

        if user_with_input_username and not user_with_input_username == request.user:
            response = Response({
                'error_code': 1,
                'error_message': 'Username is already in use.'
            })
            return response
        elif not serializer.is_valid():
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return response

        serializer.save()
        response = Response(serializer.data)
        return response

class UserStatsView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username__iexact=username)
        except:
            response = Response("User not found.", status=status.HTTP_404_NOT_FOUND)
            return response
        
        serializer = UserStatsSerializer(user)
        response = Response(serializer.data)
        return response

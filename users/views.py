from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import RegisterSerializer

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

class LoginView(TokenObtainPairView):
    """Takes a set of user credentials. 
    If the credentials are valid, 
    returns an access and refresh JSON web token pair."""

    serializer_class = TokenObtainPairSerializer

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

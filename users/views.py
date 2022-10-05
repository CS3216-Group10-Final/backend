from rest_framework import generics
from rest_framework.response import Response

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

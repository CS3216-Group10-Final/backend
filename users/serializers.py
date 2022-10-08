from rest_framework import serializers

from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], 
            validated_data['email'], 
            validated_data['password']
        )

        return user

class UserSerializer(serializers.ModelSerializer):
    profile_picture_link = serializers.ImageField(
        use_url=True, 
        required=False, 
        allow_empty_file=True,
        allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'profile_picture_link']
        extra_kwargs = {'username': {'read_only': True}}
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

class UserStatsSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(source='get_average_rating', read_only=True)
    game_status_distribution = serializers.DictField(
        source='get_game_status_distribution', 
        child=serializers.IntegerField(), 
        read_only=True)
    # game_status_distribution = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'average_rating',
            'game_status_distribution',
        ]
    
    # def get_game_status_distribution(self, obj):
        # return {1: 1}
        # return {int(key) : value for key, value in obj.get_game_status_distribution().items()}
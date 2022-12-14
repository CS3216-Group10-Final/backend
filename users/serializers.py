from rest_framework import serializers

from .models import User
from badges.serializers import BadgeEntrySerializer

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

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password']

class GoogleLoginSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    error = serializers.CharField(required=False)

class UserSerializer(serializers.ModelSerializer):
    profile_picture_link = serializers.ImageField(
        use_url=True, 
        required=False, 
        allow_empty_file=True,
        allow_null=True)
    badges = BadgeEntrySerializer(many=True, read_only=True, source='badge_entries')
    is_following = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_picture_link', 'badges', 'is_following']
    
    def get_is_following(self, obj):
        request_user = self.context.get('request_user')
        if request_user:
            return obj.incoming_follows.filter(follower=request_user.id).exists()
        else:
            return True

class PrivateUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_picture_link', 'badges', 'is_following', 'steamid', 'personaname']

class UserStatsSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(source='get_average_rating', read_only=True)
    total_games_played = serializers.IntegerField(source='get_total_games_played', read_only=True)
    game_status_distribution = serializers.DictField(
        source='get_game_status_distribution', 
        child=serializers.IntegerField(), 
        read_only=True)
    game_genre_distribution = serializers.DictField(
        source='get_game_genre_distribution', 
        child=serializers.IntegerField(), 
        read_only=True)
    platform_distribution = serializers.DictField(
        source='get_platform_distribution', 
        child=serializers.IntegerField(), 
        read_only=True)
    release_year_distribution = serializers.DictField(
        source='get_release_year_distribution', 
        child=serializers.IntegerField(), 
        read_only=True)
    play_year_distribution = serializers.DictField(
        source='get_play_year_distribution', 
        child=serializers.IntegerField(), 
        read_only=True)
    
    class Meta:
        model = User
        fields = [
            'average_rating',
            'total_games_played',
            'game_status_distribution',
            'game_genre_distribution',
            'platform_distribution',
            'release_year_distribution',
            'play_year_distribution',
        ]
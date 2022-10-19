from rest_framework import serializers

from .models import BadgeEntry

class BadgeEntrySerializer(serializers.ModelSerializer):
    badge_name = serializers.CharField(source='badge.name', read_only=True)
    badge_picture = serializers.ImageField(source='badge.picture', use_url=True, read_only=True)
    badge_description = serializers.CharField(source='badge.description', read_only=True)

    class Meta:
        model = BadgeEntry
        exclude = ['user', 'badge',]
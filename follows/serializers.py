from rest_framework import serializers

from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ("id", "user_id", "followed_user_id", "created_at", "updated_at")

from django.db import models
from django.contrib.postgres.fields import JSONField
from rest_framework import serializers
from rest_framework.response import Response


class Follow(models.Model):
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    followed_user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 전체 유저 목록을 불러올 때, follow여부 확인
class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()

    def get_following(self, obj):
        user = self.context["request"].user
        return obj.following.filter(id=user.id).exists()

    class Meta:
        model = Follow
        fields = (
            "id",
            "follower",
            "following",
        )


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
    is_hidden = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostSerializer(serializers.ModelSerializer):
    is_hidden = serializers.BooleanField(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "author",
            "is_hidden",
        )


def posts_create(request):
    data = request.data
    data["author"] = request.user.id
    serializer = PostSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


def posts_update(request, post_id):
    post = Post.objects.get(id=post_id)
    data = request.data
    data["is_hidden"] = data.get("is_hidden", False)
    serializer = PostSerializer(post, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

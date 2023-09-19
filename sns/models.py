from django.db import models
from django.contrib.postgres.fields import JSONField
from rest_framework import serializers


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


class FollowsViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


# GET /api/follows
def follows_list(request):
    follows = Follow.objects.all()
    serializer = FollowSerializer(follows, many=True)
    return Response(serializer.data)


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


# POST /api/posts
def posts_create(request):
    data = request.data
    data["author"] = request.user.id
    serializer = PostSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# PUT /api/posts/<post_id>
def posts_update(request, post_id):
    post = Post.objects.get(id=post_id)
    data = request.data
    data["is_hidden"] = data.get("is_hidden", False)
    serializer = PostSerializer(post, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

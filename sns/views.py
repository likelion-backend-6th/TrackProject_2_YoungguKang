from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Post, Follow
from .serializers import PostSerializer, FollowSerializer


class PostsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # 모든 게시글을 조회합니다.
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 새 게시글을 작성합니다.
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FollowsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # 팔로우하는 사람 목록을 조회합니다.
        follows = Follow.objects.filter(user=request.user)
        serializer = FollowSerializer(follows, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 팔로우합니다.
        user = request.data["user_id"]
        follow = Follow(user=request.user, followed_user_id=user)
        follow.save()
        return Response(status=201)

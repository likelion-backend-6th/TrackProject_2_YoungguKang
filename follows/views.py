from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Follow
from .serializers import FollowSerializer


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

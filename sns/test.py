from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Follow
from django.urls import reverse
from rest_framework.status import status


class PostsViewTest(TestCase):
    def test_get_all_posts(self):
        # 게시글을 2개 생성합니다.
        post1 = Post.objects.create(title="제목1", content="내용1")
        post2 = Post.objects.create(title="제목2", content="내용2")

        # 모든 게시글을 조회합니다.
        response = self.client.get("/api/posts/")

        # 응답 코드가 200임을 확인합니다.
        self.assertEqual(response.status_code, 200)

        # 응답 본문에서 게시글 2개가 반환되었는지 확인합니다.
        posts = response.json()
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]["title"], "제목1")
        self.assertEqual(posts[1]["title"], "제목2")

    def test_create_post(self):
        # 게시글을 생성합니다.
        post_data = {"title": "제목", "content": "내용"}
        response = self.client.post("/api/posts/", data=post_data)

        # 응답 코드가 201임을 확인합니다.
        self.assertEqual(response.status_code, 201)

        # 응답 본문에서 게시글이 반환되었는지 확인합니다.
        post = response.json()
        self.assertEqual(post["title"], "제목")
        self.assertEqual(post["content"], "내용")

    def test_update_post(self):
        # 게시글을 생성합니다.
        post = Post.objects.create(title="제목", content="내용")

        # 게시글을 수정합니다.
        updated_post_data = {"title": "수정된 제목", "content": "수정된 내용"}
        response = self.client.patch(
            "/api/posts/{}/".format(post.id), data=updated_post_data
        )

        # 응답 코드가 200임을 확인합니다.
        self.assertEqual(response.status_code, 200)

        # 게시글이 수정되었는지 확인합니다.
        post.refresh_from_db()
        self.assertEqual(post.title, "수정된 제목")
        self.assertEqual(post.content, "수정된 내용")

    def test_delete_post(self):
        # 게시글을 생성합니다.
        post = Post.objects.create(title="제목", content="내용")

        # 게시글을 삭제합니다.
        response = self.client.delete("/api/posts/{}/".format(post.id))

        # 응답 코드가 204임을 확인합니다.
        self.assertEqual(response.status_code, 204)

        # 게시글이 삭제되었는지 확인합니다.
        post.refresh_from_db()
        self.assertFalse(post.exists())

    def test_follow_unfollow(self):
        # call follow api
        self.client.force_login(self.user)
        response = self.client.post(reverse("follow"), {"following": self.user2.id})
        # check response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Follow.objects.filter(follower=self.user, following=self.user2).exists()
        )

        # call unfollow api
        self.client.force_login(self.user)
        response = self.client.post(reverse("follow"), {"following": self.user2.id})
        # check response
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Follow.objects.filter(follower=self.user, following=self.user2).exists()
        )

    def test_get_following_posts(self):
        user3 = User.objects.create_user(username="user3")
        unfollowing_user = User.objects.create_user(username="unfollowing")
        # follow user2 and user3
        Follow.objects.create(follower=self.user, following=self.user2)
        Follow.objects.create(follower=self.user, following=user3)
        # create some posts
        post_n = 5
        for i in range(post_n):
            Post.objects.create(user=self.user, content=f"test{i}")
            Post.objects.create(user=self.user2, content=f"test{i}")
            Post.objects.create(user=user3, content=f"test{i}")
            Post.objects.create(user=unfollowing_user, content=f"test{i}")
        # call get list api
        self.client.force_login(self.user)
        response = self.client.get(reverse("feed"))
        # check response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), post_n * 2)

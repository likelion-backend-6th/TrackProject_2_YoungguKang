from django.contrib import admin
from django.urls import path, include

from sns import views as follows_views
from sns import views as posts_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/follows/", follows_views.FollowsView.as_view()),
    path("api/posts/", posts_views.PostsView.as_view()),
]

from django.db import models


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

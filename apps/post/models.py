from django.db import models

from apps.account.models import Account
from apps.utils import TimeStampedModel


class Tag(TimeStampedModel):
    name = models.CharField(max_length=20)
    """
    inherited from TimeStampedModel
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    """

    class Meta:
        db_table = "tags"


class Post(TimeStampedModel):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    writer = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name="post")
    tags = models.ManyToManyField(to=Tag, blank=True, related_name="posts")
    views = models.PositiveIntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    """
    inherited from TimeStampedModel
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    """

    class Meta:
        db_table = "posts"

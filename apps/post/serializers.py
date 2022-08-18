from datetime import datetime

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.post.models import Post, Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


# api/v1/posts
class PostCreateSerializer(ModelSerializer):

    tags = TagSerializer(many=True)

    def create(self, validated_data):
        writer = self.context["user"]
        tags = validated_data.pop("tags", None)
        post = Post.objects.create(writer=writer, **validated_data)
        post.save()

        if tags:
            for i in tags:
                tag, _ = Tag.objects.get_or_create(name=i["name"])
                post.tags.add(tag)

        return post

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "tags",
            "created_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/v1/posts
class PostListSerializer(ModelSerializer):

    writer = SerializerMethodField()
    tags = TagSerializer(many=True)

    def get_writer(self, obj):
        return obj.writer.account_name

    class Meta:
        model = Post
        fields = [
            "id",
            "writer",
            "title",
            "content",
            "tags",
            "views",
            "created_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/v1/posts/<int:pk>
class PostDetailSerializer(ModelSerializer):

    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "writer",
            "title",
            "content",
            "tags",
            "views",
            "updated_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/v1/posts/<int:pk>
class PostUpdateSerializer(ModelSerializer):

    tags = TagSerializer(many=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()

        tags = validated_data.pop("tags", None)
        if tags:
            instance.tags.clear()
            for i in tags:
                tag, _ = Tag.objects.get_or_create(name=i["name"])
                instance.tags.add(tag)
            instance.save()
        return instance

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "tags",
            "updated_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/v1/posts/<int:pk>
class PostDeleteSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        if instance.is_deleted:
            raise serializers.ValidationError("이미 삭제된 게시물입니다.")
        instance.is_deleted = True
        instance.deleted_at = datetime.now()
        instance.save()
        return instance

    class Meta:
        model = Post
        fields = [
            "id",
            "is_deleted",
            "deleted_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/v1/posts/<int:pk>
class PostRestoreSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        if not instance.is_deleted:
            raise serializers.ValidationError("삭제되지 않은 게시물입니다.")
        instance.is_deleted = False
        instance.deleted_at = None
        instance.save()
        return instance

    class Meta:
        model = Post
        fields = [
            "id",
            "is_deleted",
            "deleted_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}

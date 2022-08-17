from rest_framework.serializers import ModelSerializer

from apps.post.models import Post, Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


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

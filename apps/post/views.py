from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.post.models import Post
from apps.post.serializers import PostCreateSerializer, PostListSerializer


# api/v1/posts
class PostView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data, context={"user": request.user})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "게시글 작성에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            search = request.GET.get("search", None)
            tag = request.GET.get("tag", None)
            sort = request.GET.get("sort", "recent")
            offset = int(request.GET.get("offset", 0))
            limit = int(request.GET.get("limit", 10))

            q = Q()

            if search:
                q |= Q(title__icontains=search)
                q |= Q(content__icontains=search)

            if tag:
                tags = tag.split(",")
                q &= Q(tags__name__in=tags)

            sort_set = {
                "recent": "-created_at",
                "most_viewed": "-views",
            }

            posts = (
                Post.objects.exclude(is_deleted=True)
                .select_related("writer")
                .prefetch_related("tags")
                .filter(q)
                .order_by(sort_set[sort])[offset : offset + limit]
            )
            serializer = PostListSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"message": "Key error"})

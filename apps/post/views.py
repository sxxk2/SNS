from django.db.models import Q
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.post.models import Post
from apps.post.permissions import IsOwnerOrReadOnly
from apps.post.serializers import (
    PostCreateSerializer,
    PostDeleteSerializer,
    PostDetailSerializer,
    PostListSerializer,
    PostRestoreSerializer,
    PostUpdateSerializer,
)
from apps.post.swagger import PostDeleteResponse, limit, offset, search, sort, tag


# api/v1/posts
class PostView(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=PostCreateSerializer)
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data, context={"user": request.user})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "게시글 작성에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={200: PostListSerializer(many=True)}, manual_parameters=[search, tag, sort, offset, limit]
    )
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


# api/v1/posts/<int:pk>
class PostDetailView(RetrieveUpdateAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    allowed_methods = ["GET", "PATCH", "DELETE"]

    def get_queryset(self):
        queryset = Post.objects.filter(pk=self.kwargs["pk"])
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostDetailSerializer
        elif self.request.method == "PATCH":
            return PostUpdateSerializer
        elif self.request.method == "DELETE":
            return PostDeleteSerializer

    def retrieve(self, request, *args, **kwargs):
        post = self.get_object()
        post.views += 1
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=PostDeleteResponse)
    def delete(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# api/v1/posts/<int:pk>/restore
class PostRestoreView(UpdateAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    allowed_methods = ["PATCH"]

    def get_queryset(self):
        queryset = Post.objects.filter(is_deleted=True, pk=self.kwargs["pk"])
        return queryset

    def get_object(self):
        filter_kwargs = {self.lookup_field: self.kwargs["pk"]}
        obj = get_object_or_404(self.get_queryset(), **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return PostRestoreSerializer

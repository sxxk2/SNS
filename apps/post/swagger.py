from drf_yasg import openapi

from apps.post.serializers import PostDeleteSerializer

PostDeleteResponse = {
    200: openapi.Response("게시물 삭제 성공", PostDeleteSerializer),
}

search = openapi.Parameter("search", openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING)
tag = openapi.Parameter("tag", openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING)
sort = openapi.Parameter("sort", openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING)
offset = openapi.Parameter("offset", openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING)
limit = openapi.Parameter("limit", openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING)

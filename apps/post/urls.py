from django.urls import path

from apps.post.views import PostDetailView, PostRestoreView, PostView

app_name = "post"

urlpatterns = [
    path("", PostView.as_view(), name="post"),
    path("/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("/<int:pk>/restore", PostRestoreView.as_view(), name="post_restore"),
]

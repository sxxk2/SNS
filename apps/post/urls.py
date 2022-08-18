from django.urls import path

from apps.post.views import PostDetailView, PostView

urlpatterns = [
    path("", PostView.as_view()),
    path("/<int:pk>", PostDetailView.as_view()),
]

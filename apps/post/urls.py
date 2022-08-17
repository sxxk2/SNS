from django.urls import path

from apps.post.views import PostView

urlpatterns = [
    path("", PostView.as_view()),
]

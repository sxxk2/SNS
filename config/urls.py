from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/accounts", include("apps.account.urls")),
    path("api/v1/posts", include("apps.post.urls")),
]

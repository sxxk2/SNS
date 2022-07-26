from django.urls import path

from apps.account.views import SignUpView

urlpatterns = [
    path("signup", SignUpView.as_view()),
]

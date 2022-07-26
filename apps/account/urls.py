from django.urls import path

from apps.account.views import SignInView, SignUpView

urlpatterns = [
    path("signup", SignUpView.as_view()),
    path("signin", SignInView.as_view()),
]

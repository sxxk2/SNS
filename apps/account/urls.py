from django.urls import path

from apps.account.views import AccountRestoreView, AccountView, KakaoSignInView, SignInView, SignUpView

urlpatterns = [
    path("signup", SignUpView.as_view()),
    path("signin", SignInView.as_view()),
    path("kakao/signin", KakaoSignInView.as_view()),
    path("restore", AccountRestoreView.as_view()),
    path("<int:pk>", AccountView.as_view()),
]

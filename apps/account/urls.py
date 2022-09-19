from django.urls import path

from apps.account.views import AccountRestoreView, AccountView, KakaoSignInView, SignInView, SignUpView

app_name = "account"

urlpatterns = [
    path("/signup", SignUpView.as_view(), name="account_signup"),
    path("/signin", SignInView.as_view(), name="account_signin"),
    path("/kakao/signin", KakaoSignInView.as_view(), name="account_signin_kakao"),
    path("/<int:pk>", AccountView.as_view(), name="account_detail"),
    path("/restore", AccountRestoreView.as_view(), name="account_restore"),
]

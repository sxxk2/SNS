from drf_yasg import openapi

from apps.account.serializers import AccountDeleteSerializer

SignUpResponse = {
    200: openapi.Response(description="회원가입 성공", examples={"application/json": {"message": "회원가입에 성공했습니다."}}),
    400: openapi.Response(description="회원가입 실패", examples={"application/json": {"message": "회원가입에 실패했습니다."}}),
}


SignInResponse = {
    200: openapi.Response(
        description="로그인 성공",
        examples={
            "application/json": {
                "message": "로그인 되었습니다.",
                "access_token": "string",
                "refresh_token": "string",
            }
        },
    ),
    400: openapi.Response(
        description="로그인 실패", examples={"application/json": {"non_field_errors": ["아이디 또는 비빌먼호를 잘못 입력했습니다."]}}
    ),
}


AccountDeleteResponse = {
    200: openapi.Response("회원 탈퇴 성공", AccountDeleteSerializer),
}


AccountRestoreSchema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "email": openapi.Schema(type=openapi.TYPE_STRING),
        "password": openapi.Schema(type=openapi.TYPE_STRING),
    },
)


AccountRestoreResponse = {
    200: openapi.Response(description="회원 탈퇴 복구 성공", examples={"application/json": {"message": "계정이 복구되었습니다."}}),
    400: openapi.Response(description="회원 탈퇴 복구 실패", examples={"application/json": ["아이디 또는 비밀번호를 잘못 입력했습니다."]}),
}


KakaoSignInResponse = {
    200: openapi.Response(
        description="로그인 성공",
        examples={
            "application/json": {
                "message": "로그인 되었습니다.",
                "access_token": "string",
                "refresh_token": "string",
            }
        },
    ),
    400: openapi.Response(description="로그인 실패", examples={"application/json": {"message": "Key error"}}),
}

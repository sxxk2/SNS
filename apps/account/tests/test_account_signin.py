import json

import pytest
from rest_framework.reverse import reverse


def test_account_signin_success(client, account):
    url = reverse("account:account_signin")

    data = {"email": "test@gmail.com", "password": "test"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["message"] == "로그인 되었습니다."
    assert data["access_token"]
    assert data["refresh_token"]


@pytest.mark.django_db
def test_account_signin_with_invalid_email(client):
    url = reverse("account:account_signin")

    data = {"email": "test_not_exsist@gmail.com", "password": "test"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["non_field_errors"][0] == "아이디 또는 비빌먼호를 잘못 입력했습니다."


@pytest.mark.django_db
def test_account_signin_with_invalid_password(client):
    url = reverse("account:account_signin")

    data = {"email": "test@gmail.com", "password": "test_incorrect_password"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["non_field_errors"][0] == "아이디 또는 비빌먼호를 잘못 입력했습니다."


def test_account_signin_with_deleted_account(client, deleted_account):
    url = reverse("account:account_signin")

    data = {"email": "deleted_account_test@gmail.com", "password": "test"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["non_field_errors"][0] == "아이디 또는 비빌먼호를 잘못 입력했습니다."

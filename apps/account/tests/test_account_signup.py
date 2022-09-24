import json

import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_account_signup_success(client):
    url = reverse("account:account_signup")

    data = {"email": "test@gmail.com", "account_name": "test", "password": "test"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 201
    assert data["message"] == "회원가입에 성공했습니다."


@pytest.mark.django_db
def test_account_signup_with_invalid_email(client):
    url = reverse("account:account_signup")

    data = {"email": "invalid_email_format", "account_name": "test", "password": "test"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["message"] == "회원가입에 실패했습니다."


def test_account_signup_with_existed_email(client, account):
    url = reverse("account:account_signup")

    data = {"email": "test@gmail.com", "account_name": "test", "password": "test"}  # 중복

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["message"] == "회원가입에 실패했습니다."


def test_account_signup_with_existed_account_name(client, account):
    url = reverse("account:account_signup")

    data = {"email": "test_fail@gmail.com", "account_name": "test", "password": "test"}  # 중복

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["message"] == "회원가입에 실패했습니다."


@pytest.mark.django_db
def test_account_signup_without_email(client):
    url = reverse("account:account_signup")

    data = {"account_name": "test", "password": "test"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["message"] == "회원가입에 실패했습니다."


def test_account_signup_without_account_name(client, account):
    url = reverse("account:account_signup")

    data = {"email": "test@gmail.com", "password": "test"}

    response = client.post(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["message"] == "회원가입에 실패했습니다."

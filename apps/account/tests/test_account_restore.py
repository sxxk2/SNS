import json

import pytest
from rest_framework.reverse import reverse


def test_account_restore_success(client, deleted_account):
    url = reverse("account:account_restore")

    data = {"email": "test_deleted_account@gmail.com", "password": "test"}

    response = client.patch(url, data=data, content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["message"] == "계정이 복구되었습니다."


@pytest.mark.django_db
def test_account_restore_with_incorrect_email(client):
    url = reverse("account:account_restore")

    data = {"email": "test_not_exsist@gmail.com", "password": "test"}

    response = client.patch(url, data=data, content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data[0] == "아이디 또는 비밀번호를 잘못 입력했습니다."


@pytest.mark.django_db
def test_account_restore_with_incorrect_password(client):
    url = reverse("account:account_restore")

    data = {"email": "test_deleted_account@gmail.com", "password": "incorrect_password"}

    response = client.patch(url, data=data, content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data[0] == "아이디 또는 비밀번호를 잘못 입력했습니다."


def test_account_restore_with_undeleted_account(client, account):
    url = reverse("account:account_restore")

    data = {"email": "test@gmail.com", "password": "test"}

    response = client.patch(url, data=data, content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data[0] == "잘못된 접근입니다."

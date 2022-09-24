import json

from rest_framework.reverse import reverse
from rest_framework.test import APIClient


def test_account_detail_read_success(account):
    url = reverse("account:account_detail", kwargs={"pk": account.pk})

    client = APIClient()
    client.force_authenticate(user=account)

    response = client.get(url)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["id"] == account.id
    assert data["account_name"] == account.account_name
    assert data["user_name"] == account.user_name
    assert data["bio"] == account.bio
    assert data["website"] == account.website
    assert data["updated_at"]


def test_account_detail_update_success(account):
    url = reverse("account:account_detail", kwargs={"pk": account.pk})

    client = APIClient()
    client.force_authenticate(user=account)

    data = {
        "account_name": "test_account_name_change",
        "user_name": "test_user_name_change",
        "bio": "test_bio_change",
        "website": "test_website_change",
    }

    response = client.patch(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["id"] == account.id
    assert data["account_name"] == "test_account_name_change"
    assert data["user_name"] == "test_user_name_change"
    assert data["bio"] == "test_bio_change"
    assert data["website"] == "test_website_change"
    assert data["updated_at"]


def test_account_detail_update_with_invalid_account(account, account_b):
    url = reverse("account:account_detail", kwargs={"pk": account.pk})

    client = APIClient()
    client.force_authenticate(user=account_b)

    data = {"account_name": "should_not_work"}

    response = client.patch(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 403
    assert data["detail"] == "이 작업을 수행할 권한(permission)이 없습니다."


def test_account_detail_delete_success(account):
    url = reverse("account:account_detail", kwargs={"pk": account.pk})

    client = APIClient()
    client.force_authenticate(user=account)

    response = client.delete(url)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["id"] == account.id
    assert data["is_active"] == False
    assert data["deleted_at"]


def test_account_detail_delete_with_invalid_account(account, account_b):
    url = reverse("account:account_detail", kwargs={"pk": account.pk})

    client = APIClient()
    client.force_authenticate(user=account_b)

    response = client.delete(url)

    data = json.loads(response.content)

    assert response.status_code == 403
    assert data["detail"] == "이 작업을 수행할 권한(permission)이 없습니다."

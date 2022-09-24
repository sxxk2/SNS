import json

from rest_framework.reverse import reverse
from rest_framework.test import APIClient


def test_post_restore_success(account, deleted_post):
    url = reverse("post:post_restore", kwargs={"pk": deleted_post.pk})

    client = APIClient()
    client.force_authenticate(user=account)

    response = client.patch(url)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["id"] == deleted_post.id
    assert data["is_deleted"] == False
    assert data["deleted_at"] == None  # noqa


def test_post_restore_with_invalid_account(account_b, deleted_post):
    url = reverse("post:post_restore", kwargs={"pk": deleted_post.pk})

    client = APIClient()
    client.force_authenticate(user=account_b)

    response = client.patch(url)

    data = json.loads(response.content)

    assert response.status_code == 403
    assert data["detail"] == "이 작업을 수행할 권한(permission)이 없습니다."


def test_post_restore_with_undeleted_post(account, post):
    url = reverse("post:post_restore", kwargs={"pk": post.pk})

    client = APIClient()
    client.force_authenticate(user=account)

    response = client.patch(url)

    data = json.loads(response.content)

    assert response.status_code == 404
    assert data["detail"] == "찾을 수 없습니다."

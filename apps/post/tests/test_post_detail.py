import json

from rest_framework.reverse import reverse
from rest_framework.test import APIClient


def test_post_detail_read_success(account, post):
    url = reverse("post:post_detail", kwargs={"pk": post.pk})

    client = APIClient()
    client.force_authenticate(user=account)

    response = client.get(url)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["id"] == post.id
    assert data["writer"] == account.id
    assert data["title"] == post.title
    assert data["content"] == post.content
    assert data["tags"][0]["name"] == "#test_tag"
    assert data["views"] == 1
    assert data["updated_at"]


def test_post_detail_read_without_authentication(account, post):
    url = reverse("post:post_detail", kwargs={"pk": post.pk})

    client = APIClient()

    response = client.get(url)

    data = json.loads(response.content)

    assert response.status_code == 401
    assert data["detail"] == "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."


def test_post_detail_update_success(account, post):
    url = reverse("post:post_detail", kwargs={"pk": post.pk})

    client = APIClient()
    client.force_authenticate(user=account)

    data = {"title": "test_title_change", "content": "test_content_change"}

    response = client.patch(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["id"] == post.id
    assert data["title"] == "test_title_change"
    assert data["content"] == "test_content_change"
    assert data["tags"][0]["name"] == "#test_tag"
    assert data["updated_at"]


def test_post_detail_update_with_invalid_account(account_b, post):
    url = reverse("post:post_detail", kwargs={"pk": post.pk})

    client = APIClient()
    client.force_authenticate(user=account_b)

    data = {"title": "test_title_change", "content": "test_content_change"}

    response = client.patch(url, data=data)

    data = json.loads(response.content)

    assert response.status_code == 403
    assert data["detail"] == "이 작업을 수행할 권한(permission)이 없습니다."


def test_post_detail_delete_success(account, post):
    url = reverse("post:post_detail", kwargs={"pk": post.pk})

    client = APIClient()
    client.force_authenticate(user=account)

    response = client.delete(url)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data["id"] == post.id
    assert data["is_deleted"] == True
    assert data["deleted_at"]


def test_post_detail_delete_with_invalid_account(account_b, post):
    url = reverse("post:post_detail", kwargs={"pk": post.pk})

    client = APIClient()
    client.force_authenticate(user=account_b)

    response = client.delete(url)

    data = json.loads(response.content)

    assert response.status_code == 403
    assert data["detail"] == "이 작업을 수행할 권한(permission)이 없습니다."


def test_post_detail_delete_with_deleted_post(account, deleted_post):
    url = reverse("post:post_detail", kwargs={"pk": deleted_post.pk})

    client = APIClient()
    client.force_authenticate(user=account)

    response = client.delete(url)

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data[0] == "이미 삭제된 게시물입니다."

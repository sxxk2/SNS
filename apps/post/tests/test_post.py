import json

from rest_framework.reverse import reverse
from rest_framework.test import APIClient


def test_post_create_success(account):
    url = reverse("post:post")

    client = APIClient()
    client.force_authenticate(user=account)

    data = {"title": "test_title", "content": "test_content", "tags": [{"name": "#test_tag"}]}

    response = client.post(url, data=json.dumps(data), content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 201
    assert data["title"] == "test_title"
    assert data["content"] == "test_content"
    assert data["tags"][0]["name"] == "#test_tag"


def test_post_create_without_authentication(account):
    url = reverse("post:post")

    client = APIClient()

    data = {"title": "test_title", "content": "test_content", "tags": [{"name": "#test_tag"}]}

    response = client.post(url, data=json.dumps(data), content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 401
    assert data["detail"] == "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."


def test_post_create_without_data(account):
    url = reverse("post:post")

    client = APIClient()
    client.force_authenticate(user=account)

    data = {}

    response = client.post(url, data=json.dumps(data), content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["content"][0] == "이 필드는 필수 항목입니다."
    assert data["title"][0] == "이 필드는 필수 항목입니다."
    assert data["tags"][0] == "이 필드는 필수 항목입니다."


def test_post_create_without_title(account):
    url = reverse("post:post")

    client = APIClient()
    client.force_authenticate(user=account)

    data = {"content": "test_content", "tags": [{"name": "#test_tag"}]}

    response = client.post(url, data=json.dumps(data), content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["title"][0] == "이 필드는 필수 항목입니다."


def test_post_create_without_content(account):
    url = reverse("post:post")

    client = APIClient()
    client.force_authenticate(user=account)

    data = {"title": "test_title", "tags": [{"name": "#test_tag"}]}

    response = client.post(url, data=json.dumps(data), content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["content"][0] == "이 필드는 필수 항목입니다."


def test_post_create_without_tags(account):
    url = reverse("post:post")

    client = APIClient()
    client.force_authenticate(user=account)

    data = {
        "title": "test_title",
        "content": "test_content",
    }

    response = client.post(url, data=json.dumps(data), content_type="application/json")

    data = json.loads(response.content)

    assert response.status_code == 400
    assert data["tags"][0] == "이 필드는 필수 항목입니다."


def test_post_detail_read_success(account, post):
    url = reverse("post:post")

    client = APIClient()
    client.force_authenticate(user=account)

    response = client.get(url)

    data = json.loads(response.content)

    assert response.status_code == 200
    assert data[0]["id"] == post.id
    assert data[0]["writer"] == account.account_name
    assert data[0]["title"] == post.title
    assert data[0]["content"] == post.content
    assert data[0]["tags"][0]["name"] == "#test_tag"
    assert data[0]["content"] == post.content
    assert data[0]["views"] == post.views
    assert data[0]["created_at"]


def test_post_detail_read_without_authentication(account, post):
    url = reverse("post:post")

    client = APIClient()

    response = client.get(url)

    data = json.loads(response.content)

    assert response.status_code == 401
    assert data["detail"] == "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."

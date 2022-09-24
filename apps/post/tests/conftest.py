import pytest

from apps.post.models import Post, Tag


@pytest.fixture
def account(django_user_model):
    account = django_user_model.objects.create_user(
        email="test@gmail.com",
        account_name="test",
    )
    account.set_password("test")
    account.save()
    return account


@pytest.fixture
def account_b(django_user_model):
    account = django_user_model.objects.create_user(
        email="test_b@gmail.com",
        account_name="test_b",
    )
    account.set_password("test")
    account.save()
    return account


@pytest.fixture
def deleted_account(django_user_model):
    deleted_account = django_user_model.objects.create(
        email="deleted_account_test@gmail.com",
        account_name="deleted_account_test",
        is_active=False,
    )
    deleted_account.set_password("test")
    deleted_account.save()
    return deleted_account


@pytest.fixture
def tag():
    tag = Tag.objects.create(name="#test_tag")
    return tag


@pytest.fixture
def post(account, tag):
    post = Post.objects.create(writer_id=account.id, title="test_title", content="test_content")
    post.tags.add(tag)
    return post


@pytest.fixture
def deleted_post(account):
    post = Post.objects.create(
        writer_id=account.id, title="test_deleted_title", content="test_deleted_content", is_deleted=True
    )
    return post

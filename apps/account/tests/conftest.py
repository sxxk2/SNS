import pytest


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
        email="test_deleted_account@gmail.com",
        account_name="test_deleted_account",
        is_active=False,
    )
    deleted_account.set_password("test")
    deleted_account.save()
    return deleted_account
